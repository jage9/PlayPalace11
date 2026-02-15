"""Client Options Profile dialog for Play Palace v9 client."""

import wx
from .enhance_wx import audio_events


class ClientOptionsDialog(wx.Dialog, audio_events.SoundBindingsMixin):
    """Dialog for managing client-side options (audio, social, etc.)."""

    def __init__(
        self,
        parent,
        config_manager,
        server_id,
        lang_codes,
        sound_manager=None,
        client_options=None,
    ):
        """Initialize the client options dialog.

        Args:
            parent: Parent window
            config_manager: ConfigManager instance
            server_id: Current server ID
            lang_codes: The iso language codes
            sound_manager: SoundManager instance (optional, for applying volume changes)
            client_options: Reference to main window's client_options dict (optional, will be updated on save)
        """
        super().__init__(parent, title="Client Options Profile", size=(600, 500))

        self.config_manager = config_manager
        self.server_id = server_id
        self.lang_codes = lang_codes
        self.sound_manager = sound_manager

        # Get current options (defaults + server overrides)
        # Use passed-in client_options if provided, otherwise load from config
        self.options = (
            client_options
            if client_options is not None
            else config_manager.get_client_options(server_id)
        )
        self.defaults = config_manager.profiles["client_options_defaults"]
        self.overrides = config_manager.profiles["servers"][server_id].get(
            "options_overrides", {}
        )

        # Build games_list from local_table/creation_notifications keys in config
        local_table = self.options.get("local_table", {})
        creation_notifications = local_table.get("creation_notifications", {})
        self.games_list = [
            {"type": game_type, "name": game_type}
            for game_type in creation_notifications.keys()
        ]

        # Get languages from language_subscriptions keys in config
        social = self.options.get("social", {})
        lang_subs = social.get("language_subscriptions", {})
        self.languages = list(lang_subs.keys()) if lang_subs else ["English"]

        # Profile mode: "server" or "default"
        self.profile_mode = "server"

        self._create_ui()
        self.CenterOnScreen()

    def get_language_code(self, name: str = "") -> str:
        """Get a language code from its name."""
        if not name:
            name = self.clientoptions["social"]["chat_input_language"]
        try:
            return tuple(self.lang_codes.keys())[
                tuple(self.lang_codes.values()).index(name)
            ]
        except ValueError:
            return ""

    def _create_ui(self):
        """Create the UI components."""
        panel = wx.Panel(self)
        self.panel = panel  # Store panel reference
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Server name display and nickname editor
        server_name = self.config_manager.get_server_display_name(self.server_id)
        server_label = wx.StaticText(panel, label=f"Options for: {server_name}")
        font = server_label.GetFont()
        font.PointSize += 2
        font = font.Bold()
        server_label.SetFont(font)
        main_sizer.Add(server_label, 0, wx.ALL | wx.CENTER, 10)

        # Profile mode toggle
        mode_label = wx.StaticText(panel, label="&Profile Selection:")
        main_sizer.Add(mode_label, 0, wx.LEFT | wx.TOP, 10)

        self.mode_radio = wx.RadioBox(
            panel,
            choices=["Server Profile", "Default Profile"],
            majorDimension=2,
            style=wx.RA_SPECIFY_COLS,
        )
        self.mode_radio.SetLabel("Profile Selection:")
        self.mode_radio.SetSelection(0)  # Server Profile by default
        self.mode_radio.Bind(wx.EVT_RADIOBOX, self.on_mode_change)
        main_sizer.Add(
            self.mode_radio, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 10
        )

        # Server nickname section
        self.nickname_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.nickname_label = wx.StaticText(panel, label="Server &Nickname:")
        self.nickname_sizer.Add(
            self.nickname_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 10
        )

        server_info = self.config_manager.get_server_by_id(self.server_id)
        current_name = server_info.get("name") or ""

        self.nickname_input = wx.TextCtrl(panel, value=current_name, size=(300, -1))
        self.nickname_sizer.Add(self.nickname_input, 1, wx.EXPAND)

        # Show server address as hint
        server_host = server_info.get("host", "")
        server_port = server_info.get("port", 8000)
        self.url_hint = wx.StaticText(panel, label=f"Address: {server_host}:{server_port}")
        font = self.url_hint.GetFont()
        font.PointSize -= 1
        self.url_hint.SetFont(font)

        main_sizer.Add(self.nickname_sizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        main_sizer.Add(self.url_hint, 0, wx.LEFT | wx.BOTTOM, 10)

        # Notebook for categories
        self.notebook = wx.Notebook(panel)

        # Audio tab
        audio_panel = self._create_audio_panel(self.notebook)
        self.notebook.AddPage(audio_panel, "Audio")

        # Social tab
        social_panel = self._create_social_panel(self.notebook)
        self.notebook.AddPage(social_panel, "Social")

        # Interface tab
        interface_panel = self._create_interface_panel(self.notebook)
        self.notebook.AddPage(interface_panel, "Interface")

        # Local Table tab
        tables_panel = self._create_tables_panel(self.notebook)
        self.notebook.AddPage(tables_panel, "Local Table")

        self.tab_names = tuple(
            [self.notebook.GetPageText(i) for i in range(self.notebook.GetPageCount())]
        )
        main_sizer.Add(self.notebook, 1, wx.EXPAND | wx.ALL, 10)

        # Buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Reset to Last Used Settings button (shown in both modes)
        reset_last_btn = wx.Button(panel, label="Reset from Last &Used Settings")
        reset_last_btn.Bind(wx.EVT_BUTTON, self.on_reset_to_last_used)
        button_sizer.Add(reset_last_btn, 0, wx.RIGHT, 5)

        # Reset to Defaults button (shown only in server mode)
        self.reset_defaults_btn = wx.Button(panel, label="&Reset from Default Profile")
        self.reset_defaults_btn.Bind(wx.EVT_BUTTON, self.on_reset_to_defaults)
        button_sizer.Add(self.reset_defaults_btn, 0, wx.RIGHT, 5)

        button_sizer.AddStretchSpacer()

        # Set as Default button (shown in server mode)
        self.set_default_btn = wx.Button(panel, label="Apply to &Default Profile")
        self.set_default_btn.Bind(wx.EVT_BUTTON, self.on_set_as_default)
        button_sizer.Add(self.set_default_btn, 0, wx.RIGHT, 5)

        # Apply to Server button (shown in default mode)
        self.apply_to_server_btn = wx.Button(panel, label="Apply to &Current Server")
        self.apply_to_server_btn.Bind(wx.EVT_BUTTON, self.on_apply_to_server)
        button_sizer.Add(self.apply_to_server_btn, 0, wx.RIGHT, 5)
        self.apply_to_server_btn.Hide()  # Hidden by default (in server mode)

        save_btn = wx.Button(panel, label="&Save All Settings")
        save_btn.SetDefault()
        button_sizer.Add(save_btn, 0, wx.RIGHT, 5)

        done_btn = wx.Button(panel, wx.ID_CANCEL, "Done")
        button_sizer.Add(done_btn, 0)

        main_sizer.Add(button_sizer, 0, wx.EXPAND | wx.ALL, 10)

        # Bind events
        save_btn.Bind(wx.EVT_BUTTON, self.on_save)
        done_btn.Bind(wx.EVT_BUTTON, self.on_done)
        self.Bind(wx.EVT_CLOSE, self.on_close)

        panel.SetSizer(main_sizer)
        self.bind_sounds(recursion=-1)  # don't need to bind sounds to every control

    def _create_audio_panel(self, parent):
        """Create the audio options panel."""
        panel = wx.Panel(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Music volume
        music_label = wx.StaticText(panel, label="&Music Volume (spin button):")
        sizer.Add(music_label, 0, wx.ALL, 10)

        self.music_spin = wx.SpinCtrl(
            panel,
            value=str(self.options["audio"]["music_volume"]),
            min=0,
            max=100,
            initial=self.options["audio"]["music_volume"],
        )
        self.music_spin.Bind(wx.EVT_SPINCTRL, self.on_music_spin_change)
        self.music_spin.Bind(wx.EVT_TEXT, self.on_music_spin_change)
        sizer.Add(self.music_spin, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 10)

        # Show if override
        if "music_volume" in self.overrides.get("audio", {}):
            music_override_label = wx.StaticText(
                panel,
                label=f"(Override - Default: {self.defaults['audio']['music_volume']}%)",
            )
            sizer.Add(music_override_label, 0, wx.LEFT | wx.BOTTOM, 10)

        # Ambience volume
        ambience_label = wx.StaticText(panel, label="&Ambience Volume (spin button):")
        sizer.Add(ambience_label, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)

        self.ambience_spin = wx.SpinCtrl(
            panel,
            value=str(self.options["audio"]["ambience_volume"]),
            min=0,
            max=100,
            initial=self.options["audio"]["ambience_volume"],
        )
        self.ambience_spin.Bind(wx.EVT_SPINCTRL, self.on_ambience_spin_change)
        self.ambience_spin.Bind(wx.EVT_TEXT, self.on_ambience_spin_change)
        sizer.Add(self.ambience_spin, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 10)

        # Show if override
        if "ambience_volume" in self.overrides.get("audio", {}):
            ambience_override_label = wx.StaticText(
                panel,
                label=f"(Override - Default: {self.defaults['audio']['ambience_volume']}%)",
            )
            sizer.Add(ambience_override_label, 0, wx.LEFT | wx.BOTTOM, 10)

        # Info text
        info_text = wx.StaticText(
            panel,
            label="Note: F7-F10 hotkeys also adjust volumes. Changes here are saved per-server.",
        )
        sizer.Add(info_text, 0, wx.ALL, 10)

        panel.SetSizer(sizer)
        return panel

    def _create_social_panel(self, parent):
        """Create the social options panel."""
        panel = wx.Panel(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)

        social = self.options.get("social", {})

        # Mute global chat checkbox
        self.mute_global_check = wx.CheckBox(panel, label="Mute &Global Chat")
        self.mute_global_check.SetValue(social.get("mute_global_chat", False))
        sizer.Add(self.mute_global_check, 0, wx.ALL, 10)

        # Mute table chat checkbox
        self.mute_table_check = wx.CheckBox(panel, label="Mute &Table Chat")
        self.mute_table_check.SetValue(social.get("mute_table_chat", False))
        sizer.Add(self.mute_table_check, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)

        # Include language filters for table chat checkbox
        self.include_lang_filters_table_check = wx.CheckBox(
            panel, label="Include Language &Filters for Table Chat"
        )
        self.include_lang_filters_table_check.SetValue(
            social.get("include_language_filters_for_table_chat", False)
        )
        sizer.Add(
            self.include_lang_filters_table_check, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 10
        )

        lang_list = []
        self.displayed_languages = []  # Track languages actually shown in the list
        for name in self.languages:
            code = self.get_language_code(name)
            if not code:
                continue
            lang_list.append(name + " " + code)
            self.displayed_languages.append(name)

        # Chat input language
        lang_label = wx.StaticText(panel, label="Chat &Input Language:")
        sizer.Add(lang_label, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)

        # Use languages from server
        self.language_choice = wx.Choice(panel, choices=self.languages)
        current_lang = social.get("chat_input_language", "English")
        if current_lang in self.languages:
            self.language_choice.SetStringSelection(current_lang)
        else:
            self.language_choice.SetSelection(0)
        sizer.Add(
            self.language_choice, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 10
        )

        # Language subscriptions
        sub_label = wx.StaticText(panel, label="&Language Channel Subscriptions:")
        sizer.Add(sub_label, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)

        lang_subs = social.get("language_subscriptions", {})
        self.lang_subscriptions_list = wx.CheckListBox(panel, choices=lang_list)

        # Check the subscribed languages
        for i, lang in enumerate(self.displayed_languages):
            if lang_subs.get(lang, False):
                self.lang_subscriptions_list.Check(i)

        self.lang_subscriptions_list.SetSelection(0)
        sizer.Add(
            self.lang_subscriptions_list,
            1,
            wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND,
            10,
        )
        self.bind_sfx_to_control(self.lang_subscriptions_list, True)

        panel.SetSizer(sizer)
        return panel

    def _create_interface_panel(self, parent):
        """Create the interface options panel."""
        panel = wx.Panel(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)

        interface = self.options.get("interface", {})

        # Invert multiline enter behavior checkbox
        self.invert_multiline_enter_check = wx.CheckBox(
            panel, label="Invert Multiline &Enter Behavior"
        )
        self.invert_multiline_enter_check.SetValue(
            interface.get("invert_multiline_enter_behavior", False)
        )
        sizer.Add(self.invert_multiline_enter_check, 0, wx.ALL, 10)

        # Play typing sounds checkbox
        self.play_typing_sounds_check = wx.CheckBox(
            panel, label="Play &Typing Sounds While Editing"
        )
        self.play_typing_sounds_check.SetValue(
            interface.get("play_typing_sounds", True)
        )
        sizer.Add(self.play_typing_sounds_check, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)

        panel.SetSizer(sizer)
        return panel

    def _create_tables_panel(self, parent):
        """Create the Local Table panel."""
        panel = wx.Panel(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)

        local_table = self.options.get("local_table", {})

        # Start table as publicly visible dropdown
        visibility_label = wx.StaticText(
            panel, label="Start table as publicly &visible:"
        )
        sizer.Add(visibility_label, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)

        self.public_visibility_choice = wx.Choice(panel, choices=("always", "ask", "never"))
        current_visibility = local_table.get("start_as_visible", "always")
        self.public_visibility_choice.SetStringSelection(current_visibility)
        sizer.Add(
            self.public_visibility_choice, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 10
        )

        # Start table with a password dropdown
        password_prompt_label = wx.StaticText(
            panel, label="Start table &with a password:"
        )
        sizer.Add(password_prompt_label, 0, wx.LEFT | wx.RIGHT, 10)

        self.password_prompt_choice = wx.Choice(panel, choices=("always", "ask", "never"))
        current_password_prompt = local_table.get("start_with_password", "never")
        self.password_prompt_choice.SetStringSelection(current_password_prompt)
        sizer.Add(
            self.password_prompt_choice, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 10
        )

        # Default password text field
        default_password_label = wx.StaticText(panel, label="Default password &text:")
        sizer.Add(default_password_label, 0, wx.LEFT | wx.RIGHT, 10)

        self.default_password_input = wx.TextCtrl(
            panel, value=local_table.get("default_password_text", "")
        )
        sizer.Add(
            self.default_password_input, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 10
        )

        # Label
        creation_subscription_label = wx.StaticText(
            panel, label="Receive &notifications when these game tables are created:"
        )
        sizer.Add(creation_subscription_label, 0, wx.ALL, 10)

        # Build game display names from server-provided list
        # games_list is a list of dicts with 'type' and 'name' keys
        game_display_names = [game["name"] for game in self.games_list]

        self.creation_subscription_list = wx.CheckListBox(panel, choices=game_display_names)

        # Check currently subscribed games
        local_table = self.options.get("local_table", {})
        creation_notifications = local_table.get("creation_notifications", {})

        for i, game_info in enumerate(self.games_list):
            game_type = game_info["type"]  # e.g., "pig", "uno", "milebymile"
            if creation_notifications.get(game_type, False):
                self.creation_subscription_list.Check(i)

        self.creation_subscription_list.SetSelection(0)
        sizer.Add(
            self.creation_subscription_list,
            1,
            wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND,
            10,
        )
        self.bind_sfx_to_control(self.creation_subscription_list, True)

        panel.SetSizer(sizer)
        return panel

    def on_music_spin_change(self, event):
        """Handle music volume spin control change - apply immediately."""
        value = self.music_spin.GetValue()
        if self.sound_manager:
            self.sound_manager.set_music_volume(value / 100.0)

    def on_ambience_spin_change(self, event):
        """Handle ambience volume spin control change - apply immediately."""
        value = self.ambience_spin.GetValue()
        if self.sound_manager:
            self.sound_manager.set_ambience_volume(value / 100.0)

    def _reset_current_tab_fields(self, data_source):
        """Reset fields in the current tab to values from the given data source.

        Args:
            data_source: Dictionary containing the values to reset to (either self.options or self.defaults)
        """
        current_page = self.notebook.GetSelection()

        if current_page == 0:  # Audio tab
            self.music_spin.SetValue(data_source["audio"]["music_volume"])
            self.ambience_spin.SetValue(data_source["audio"]["ambience_volume"])

            # Apply volume changes immediately
            if self.sound_manager:
                self.sound_manager.set_music_volume(
                    data_source["audio"]["music_volume"] / 100.0
                )
                self.sound_manager.set_ambience_volume(
                    data_source["audio"]["ambience_volume"] / 100.0
                )

        elif current_page == 1:  # Social tab
            social = data_source.get("social", {})
            self.mute_global_check.SetValue(social.get("mute_global_chat", False))
            self.mute_table_check.SetValue(social.get("mute_table_chat", False))
            self.include_lang_filters_table_check.SetValue(
                social.get("include_language_filters_for_table_chat", False)
            )

            default_lang = social.get("chat_input_language", "English")
            if default_lang in self.languages:
                self.language_choice.SetStringSelection(default_lang)
            else:
                self.language_choice.SetSelection(0)

            # Repopulate language subscriptions
            lang_subs = social.get("language_subscriptions", {})
            for i, lang in enumerate(self.displayed_languages):
                self.lang_subscriptions_list.Check(i, lang_subs.get(lang, False))

        elif current_page == 2:  # Interface tab
            interface = data_source.get("interface", {})
            self.invert_multiline_enter_check.SetValue(
                interface.get("invert_multiline_enter_behavior", False)
            )
            self.play_typing_sounds_check.SetValue(
                interface.get("play_typing_sounds", True)
            )

        elif current_page == 3:  # Local Table tab
            local_table = data_source.get("local_table", {})

            # Reset new dropdowns and text field
            current_visibility = local_table.get("start_as_visible", "always")
            self.public_visibility_choice.SetStringSelection(current_visibility)

            current_password_prompt = local_table.get("start_with_password", "never")
            self.password_prompt_choice.SetStringSelection(current_password_prompt)

            self.default_password_input.SetValue(local_table.get("default_password_text", ""))

            creation_notifications = local_table.get("creation_notifications", {})
            for i, game_info in enumerate(self.games_list):
                game_type = game_info["type"]
                self.creation_subscription_list.Check(
                    i, creation_notifications.get(game_type, False)
                )

    def on_reset_to_last_used(self, event):
        """Reset fields in current tab to last saved values."""
        # Get current tab
        current_page = self.notebook.GetSelection()
        current_tab_name = self.tab_names[current_page]

        mode_name = (
            "server profile" if self.profile_mode == "server" else "default profile"
        )
        result = wx.MessageBox(
            f"Reset {current_tab_name} settings to last saved {mode_name} values?",
            "Confirm Reset",
            wx.YES_NO | wx.ICON_QUESTION,
        )

        if result == wx.YES:
            # Reload the current saved state from config
            if self.profile_mode == "server":
                # Reload server options from config
                self.options = self.config_manager.get_client_options(self.server_id)
                data_source = self.options
            else:
                # Reload defaults from config
                self.defaults = self.config_manager.profiles["client_options_defaults"]
                data_source = self.defaults

            # Reset only the fields for the current tab
            self._reset_current_tab_fields(data_source)

    def on_reset_to_defaults(self, event):
        """Reset current tab's options to defaults for this server (server mode only)."""
        # Get current tab
        current_page = self.notebook.GetSelection()
        current_tab_name = self.tab_names[current_page]

        result = wx.MessageBox(
            f"Reset {current_tab_name} settings to defaults for this server?",
            "Confirm Reset",
            wx.YES_NO | wx.ICON_QUESTION,
        )

        if result == wx.YES:
            # Reset only the fields for the current tab using defaults
            self._reset_current_tab_fields(self.defaults)

    def on_set_as_default(self, event):
        """Set current tab's settings as the default for all servers."""
        # Get current tab
        current_page = self.notebook.GetSelection()
        current_tab_name = self.tab_names[current_page]

        # Show confirmation with specific section
        result = wx.MessageBox(
            f"Set current {current_tab_name} settings as defaults for all servers?\n\n"
            "This will overwrite existing default settings.\n"
            "Server-specific settings will remain unchanged.",
            "Confirm Set as Default",
            wx.YES_NO | wx.ICON_QUESTION,
        )

        if result == wx.YES:
            if current_page == 0:  # Audio tab
                self._apply_audio_defaults()
            elif current_page == 1:  # Social tab
                self._apply_social_defaults()
            elif current_page == 2:  # Interface tab
                self._apply_interface_defaults()
            elif current_page == 3:  # Local Table tab
                self._apply_local_table_defaults()

            # Save the updated defaults
            self.config_manager.save_profiles()

            wx.MessageBox(
                f"{current_tab_name} default settings updated successfully!",
                "Success",
                wx.OK | wx.ICON_INFORMATION,
            )

    def on_save(self, event):
        """Save changes and close dialog."""
        # Get current values from controls
        music_volume = self.music_spin.GetValue()
        ambience_volume = self.ambience_spin.GetValue()

        if self.profile_mode == "server":
            # Save server-specific settings
            nickname = self.nickname_input.GetValue().strip()

            # Save server name (use update_server to change the display name)
            if nickname:
                self.config_manager.update_server(self.server_id, name=nickname)

            # Save audio settings (as server-specific overrides)
            self.config_manager.set_client_option(
                "audio/music_volume", music_volume, self.server_id, create_mode=True
            )
            self.config_manager.set_client_option(
                "audio/ambience_volume", ambience_volume, self.server_id, create_mode=True
            )

            # Save social settings
            mute_global = self.mute_global_check.GetValue()
            mute_table = self.mute_table_check.GetValue()
            include_lang_filters_table = (
                self.include_lang_filters_table_check.GetValue()
            )
            input_lang = self.language_choice.GetStringSelection()

            self.config_manager.set_client_option(
                "social/mute_global_chat", mute_global, self.server_id, create_mode=True
            )
            self.config_manager.set_client_option(
                "social/mute_table_chat", mute_table, self.server_id, create_mode=True
            )
            self.config_manager.set_client_option(
                "social/include_language_filters_for_table_chat",
                include_lang_filters_table,
                self.server_id,
                create_mode=True,
            )
            self.config_manager.set_client_option(
                "social/chat_input_language", input_lang, self.server_id, create_mode=True
            )

            # Save language subscriptions
            lang_subs = {}
            for i, lang in enumerate(self.displayed_languages):
                lang_subs[lang] = self.lang_subscriptions_list.IsChecked(i)

            self.config_manager.set_client_option(
                "social/language_subscriptions", lang_subs, self.server_id, create_mode=True
            )

            # Save interface settings
            invert_multiline_enter = self.invert_multiline_enter_check.GetValue()
            play_typing_sounds = self.play_typing_sounds_check.GetValue()
            self.config_manager.set_client_option(
                "interface/invert_multiline_enter_behavior",
                invert_multiline_enter,
                self.server_id,
                create_mode=True,
            )
            self.config_manager.set_client_option(
                "interface/play_typing_sounds", play_typing_sounds, self.server_id, create_mode=True
            )

            # Save Local Table settings
            public_visibility = self.public_visibility_choice.GetStringSelection()
            password_prompt = self.password_prompt_choice.GetStringSelection()
            default_password = self.default_password_input.GetValue()

            self.config_manager.set_client_option(
                "local_table/start_as_visible", public_visibility, self.server_id, create_mode=True
            )
            self.config_manager.set_client_option(
                "local_table/start_with_password", password_prompt, self.server_id, create_mode=True
            )
            self.config_manager.set_client_option(
                "local_table/default_password", default_password, self.server_id, create_mode=True
            )

            # Save Local Table creation notifications (use server-provided games list)
            for i, game_info in enumerate(self.games_list):
                game_type = game_info["type"]  # e.g., "pig", "uno", "milebymile"
                is_checked = self.creation_subscription_list.IsChecked(i)
                self.config_manager.set_client_option(
                    f"local_table/creation_notifications/{game_type}", is_checked, self.server_id, create_mode=True
                )

            # Update in-memory options to stay up to date (only for server profile, not default)
            # Refresh from config manager to get the latest saved state
            self.options.clear()
            self.options.update(self.config_manager.get_client_options(self.server_id))

        else:
            # Save default profile settings
            # Update defaults - only overwrite existing keys
            self._apply_audio_defaults(music_volume, ambience_volume)

            # Save social settings
            mute_global = self.mute_global_check.GetValue()
            mute_table = self.mute_table_check.GetValue()
            include_lang_filters_table = (
                self.include_lang_filters_table_check.GetValue()
            )
            input_lang = self.language_choice.GetStringSelection()

            # Get language subscriptions
            lang_subs = {}
            for i, lang in enumerate(self.displayed_languages):
                lang_subs[lang] = self.lang_subscriptions_list.IsChecked(i)

            self._apply_social_defaults(
                mute_global,
                mute_table,
                include_lang_filters_table,
                input_lang,
                lang_subs,
            )

            # Save interface settings
            invert_multiline_enter = self.invert_multiline_enter_check.GetValue()
            play_typing_sounds = self.play_typing_sounds_check.GetValue()
            self._apply_interface_defaults(invert_multiline_enter, play_typing_sounds)

            # Save Local Table
            public_visibility = self.public_visibility_choice.GetStringSelection()
            password_prompt = self.password_prompt_choice.GetStringSelection()
            default_password = self.default_password_input.GetValue()

            creation_notifications = self._collect_creation_notifications()
            self._apply_local_table_defaults(
                public_visibility,
                password_prompt,
                default_password,
                creation_notifications,
            )

            # Save the updated defaults
            self.config_manager.save_profiles()

        # Show success message
        mode_name = (
            "Server profile" if self.profile_mode == "server" else "Default profile"
        )
        wx.MessageBox(
            f"{mode_name} settings saved successfully!",
            "Success",
            wx.OK | wx.ICON_INFORMATION,
        )

    def _apply_audio_defaults(self, music_volume: int | None = None, ambience_volume: int | None = None) -> None:
        if music_volume is None:
            music_volume = self.music_spin.GetValue()
        if ambience_volume is None:
            ambience_volume = self.ambience_spin.GetValue()
        if "audio" in self.defaults:
            if "music_volume" in self.defaults["audio"]:
                self.defaults["audio"]["music_volume"] = music_volume
            if "ambience_volume" in self.defaults["audio"]:
                self.defaults["audio"]["ambience_volume"] = ambience_volume

    def _apply_social_defaults(
        self,
        mute_global: bool | None = None,
        mute_table: bool | None = None,
        include_lang_filters_table: bool | None = None,
        input_lang: str | None = None,
        lang_subs: dict | None = None,
    ) -> None:
        if mute_global is None:
            mute_global = self.mute_global_check.GetValue()
        if mute_table is None:
            mute_table = self.mute_table_check.GetValue()
        if include_lang_filters_table is None:
            include_lang_filters_table = self.include_lang_filters_table_check.GetValue()
        if input_lang is None:
            input_lang = self.language_choice.GetStringSelection()
        if lang_subs is None:
            lang_subs = {}
            for i, lang in enumerate(self.displayed_languages):
                lang_subs[lang] = self.lang_subscriptions_list.IsChecked(i)

        if "social" in self.defaults:
            if "mute_global_chat" in self.defaults["social"]:
                self.defaults["social"]["mute_global_chat"] = mute_global
            if "mute_table_chat" in self.defaults["social"]:
                self.defaults["social"]["mute_table_chat"] = mute_table
            if "include_language_filters_for_table_chat" in self.defaults["social"]:
                self.defaults["social"]["include_language_filters_for_table_chat"] = include_lang_filters_table
            if "chat_input_language" in self.defaults["social"]:
                self.defaults["social"]["chat_input_language"] = input_lang
            if "language_subscriptions" in self.defaults["social"]:
                for lang_key in self.defaults["social"]["language_subscriptions"]:
                    if lang_key in lang_subs:
                        self.defaults["social"]["language_subscriptions"][lang_key] = lang_subs[lang_key]

    def _apply_interface_defaults(
        self,
        invert_multiline_enter: bool | None = None,
        play_typing_sounds: bool | None = None,
    ) -> None:
        if invert_multiline_enter is None:
            invert_multiline_enter = self.invert_multiline_enter_check.GetValue()
        if play_typing_sounds is None:
            play_typing_sounds = self.play_typing_sounds_check.GetValue()
        if "interface" in self.defaults:
            if "invert_multiline_enter_behavior" in self.defaults["interface"]:
                self.defaults["interface"]["invert_multiline_enter_behavior"] = invert_multiline_enter
            if "play_typing_sounds" in self.defaults["interface"]:
                self.defaults["interface"]["play_typing_sounds"] = play_typing_sounds

    def _collect_creation_notifications(self) -> dict:
        creation_notifications = {}
        for i, game_info in enumerate(self.games_list):
            game_type = game_info["type"]
            creation_notifications[game_type] = self.creation_subscription_list.IsChecked(i)
        return creation_notifications

    def _apply_local_table_defaults(
        self,
        public_visibility: str | None = None,
        password_prompt: str | None = None,
        default_password: str | None = None,
        creation_notifications: dict | None = None,
    ) -> None:
        if public_visibility is None:
            public_visibility = self.public_visibility_choice.GetStringSelection()
        if password_prompt is None:
            password_prompt = self.password_prompt_choice.GetStringSelection()
        if default_password is None:
            default_password = self.default_password_input.GetValue()
        if creation_notifications is None:
            creation_notifications = self._collect_creation_notifications()
        if "local_table" in self.defaults:
            self.defaults["local_table"]["start_as_visible"] = public_visibility
            self.defaults["local_table"]["start_with_password"] = password_prompt
            if "default_password_text" in self.defaults["local_table"]:
                self.defaults["local_table"]["default_password_text"] = default_password
            else:
                self.defaults["local_table"]["default_password"] = default_password

            default_creation_notifications = self.defaults["local_table"].setdefault(
                "creation_notifications", {}
            )
            for game_type, enabled in creation_notifications.items():
                default_creation_notifications[game_type] = enabled

    def on_done(self, event):
        """Close dialog and restore server profile volumes."""
        self._restore_volumes()
        self.EndModal(wx.ID_CANCEL)

    def on_close(self, event):
        """Handle dialog close event (including Escape key)."""
        self._restore_volumes()
        self.EndModal(wx.ID_CANCEL)

    def _restore_volumes(self):
        """Restore audio volumes to saved server profile state."""
        # Always restore server profile volumes (not defaults)
        # Re-fetch server options to get the current saved state
        server_options = self.config_manager.get_client_options(self.server_id)

        if self.sound_manager and "audio" in server_options:
            server_music = server_options["audio"]["music_volume"]
            server_ambience = server_options["audio"]["ambience_volume"]
            self.sound_manager.set_music_volume(server_music / 100.0)
            self.sound_manager.set_ambience_volume(server_ambience / 100.0)

    def on_mode_change(self, event):
        """Handle profile mode toggle."""
        selection = self.mode_radio.GetSelection()
        self.profile_mode = "server" if selection == 0 else "default"

        # Update UI visibility
        if self.profile_mode == "server":
            # Show nickname field, Reset to Defaults, and Set as Default button
            self.nickname_label.Show()
            self.nickname_input.Show()
            self.url_hint.Show()
            self.reset_defaults_btn.Show()
            self.set_default_btn.Show()
            self.apply_to_server_btn.Hide()
        else:
            # Hide nickname field, Reset to Defaults, and show Apply to Server button
            self.nickname_label.Hide()
            self.nickname_input.Hide()
            self.url_hint.Hide()
            self.reset_defaults_btn.Hide()
            self.set_default_btn.Hide()
            self.apply_to_server_btn.Show()

        # Repopulate all fields with appropriate values
        self._repopulate_fields()

        # Update layout
        self.panel.Layout()

    def _repopulate_fields(self):
        """Repopulate all fields based on current profile mode."""
        if self.profile_mode == "server":
            # Load server-specific values (defaults + overrides)
            data_source = self.options
        else:
            # Load default values only
            data_source = self.defaults

        # Repopulate audio fields
        self.music_spin.SetValue(data_source["audio"]["music_volume"])
        self.ambience_spin.SetValue(data_source["audio"]["ambience_volume"])

        # Apply volume changes immediately
        if self.sound_manager:
            self.sound_manager.set_music_volume(
                data_source["audio"]["music_volume"] / 100.0
            )
            self.sound_manager.set_ambience_volume(
                data_source["audio"]["ambience_volume"] / 100.0
            )

        # Repopulate social fields
        social = data_source.get("social", {})
        self.mute_global_check.SetValue(social.get("mute_global_chat", False))
        self.mute_table_check.SetValue(social.get("mute_table_chat", False))
        self.include_lang_filters_table_check.SetValue(
            social.get("include_language_filters_for_table_chat", False)
        )

        default_lang = social.get("chat_input_language", "English")
        if default_lang in self.languages:
            self.language_choice.SetStringSelection(default_lang)
        else:
            self.language_choice.SetSelection(0)

        # Repopulate language subscriptions
        lang_subs = social.get("language_subscriptions", {})
        for i, lang in enumerate(self.displayed_languages):
            self.lang_subscriptions_list.Check(i, lang_subs.get(lang, False))

        # Repopulate interface fields
        interface = data_source.get("interface", {})
        self.invert_multiline_enter_check.SetValue(
            interface.get("invert_multiline_enter_behavior", False)
        )
        self.play_typing_sounds_check.SetValue(
            interface.get("play_typing_sounds", True)
        )

        # Repopulate Local Table
        local_table = data_source.get("local_table", {})

        table_choices = ["always", "ask", "never"]
        current_visibility = local_table.get("start_as_visible", "ask")
        if current_visibility in table_choices:
            self.public_visibility_choice.SetStringSelection(current_visibility)
        else:
            self.public_visibility_choice.SetStringSelection("ask")

        current_password_prompt = local_table.get("start_with_password", "ask")
        if current_password_prompt in table_choices:
            self.password_prompt_choice.SetStringSelection(current_password_prompt)
        else:
            self.password_prompt_choice.SetStringSelection("ask")

        self.default_password_input.SetValue(local_table.get("default_password", ""))

        creation_notifications = local_table.get("creation_notifications", {})
        for i, game_info in enumerate(self.games_list):
            game_type = game_info["type"]
            self.creation_subscription_list.Check(i, creation_notifications.get(game_type, False))

    def on_apply_to_server(self, event):
        """Apply default settings to the current server for the selected tab."""
        # Get current tab
        current_page = self.notebook.GetSelection()
        current_tab_name = self.tab_names[current_page]

        # Show confirmation
        result = wx.MessageBox(
            f"Apply default {current_tab_name} settings to this server?\n\n"
            "This will overwrite the current server-specific settings for this section, without updating the defaults.",
            "Confirm Apply to Server",
            wx.YES_NO | wx.ICON_QUESTION,
        )

        if result == wx.YES:
            # Apply defaults to server based on current tab
            if current_page == 0:  # Audio tab
                music_volume = self.defaults["audio"]["music_volume"]
                ambience_volume = self.defaults["audio"]["ambience_volume"]

                self.config_manager.set_client_option(
                    "audio/music_volume", music_volume, self.server_id, create_mode=True
                )
                self.config_manager.set_client_option(
                    "audio/ambience_volume", ambience_volume, self.server_id, create_mode=True
                )

                # Update local options cache
                self.options["audio"]["music_volume"] = music_volume
                self.options["audio"]["ambience_volume"] = ambience_volume

            elif current_page == 1:  # Social tab
                social_defaults = self.defaults.get("social", {})

                self.config_manager.set_client_option(
                    "social/mute_global_chat",
                    social_defaults.get("mute_global_chat", False),
                    self.server_id,
                    create_mode=True,
                )
                self.config_manager.set_client_option(
                    "social/mute_table_chat",
                    social_defaults.get("mute_table_chat", False),
                    self.server_id,
                    create_mode=True,
                )
                self.config_manager.set_client_option(
                    "social/include_language_filters_for_table_chat",
                    social_defaults.get(
                        "include_language_filters_for_table_chat", False
                    ),
                    self.server_id,
                    create_mode=True,
                )
                self.config_manager.set_client_option(
                    "social/chat_input_language",
                    social_defaults.get("chat_input_language", "English"),
                    self.server_id,
                    create_mode=True,
                )
                self.config_manager.set_client_option(
                    "social/language_subscriptions",
                    social_defaults.get("language_subscriptions", {}),
                    self.server_id,
                    create_mode=True,
                )

                # Update local options cache
                self.options["social"] = social_defaults.copy()

            elif current_page == 2:  # Interface tab
                interface_defaults = self.defaults.get("interface", {})

                self.config_manager.set_client_option(
                    "interface/invert_multiline_enter_behavior",
                    interface_defaults.get("invert_multiline_enter_behavior", False),
                    self.server_id,
                    create_mode=True,
                )
                self.config_manager.set_client_option(
                    "interface/play_typing_sounds",
                    interface_defaults.get("play_typing_sounds", True),
                    self.server_id,
                    create_mode=True,
                )

                # Update local options cache
                self.options["interface"] = interface_defaults.copy()

            elif current_page == 3:  # Local Table tab
                local_table_defaults = self.defaults.get("local_table", {})

                # Apply new settings
                public_visibility = local_table_defaults.get("start_as_visible", "ask")
                password_prompt = local_table_defaults.get("start_with_password", "ask")
                default_password = local_table_defaults.get("default_password", "")

                self.config_manager.set_client_option(
                    "local_table/start_as_visible", public_visibility, self.server_id, create_mode=True
                )
                self.config_manager.set_client_option(
                    "local_table/start_with_password", password_prompt, self.server_id, create_mode=True
                )
                self.config_manager.set_client_option(
                    "local_table/default_password", default_password, self.server_id, create_mode=True
                )

                creation_notifications_defaults = local_table_defaults.get("creation_notifications", {})

                for game_type, enabled in creation_notifications_defaults.items():
                    self.config_manager.set_client_option(
                        f"local_table/creation_notifications/{game_type}", enabled, self.server_id, create_mode=True
                    )

                # Update local options cache
                if "local_table" not in self.options:
                    self.options["local_table"] = {}
                self.options["local_table"]["start_as_visible"] = public_visibility
                self.options["local_table"]["start_with_password"] = password_prompt
                self.options["local_table"]["default_password"] = default_password
                self.options["local_table"]["creation_notifications"] = creation_notifications_defaults.copy()

            wx.MessageBox(
                f"{current_tab_name} settings applied to server successfully!",
                "Success",
                wx.OK | wx.ICON_INFORMATION,
            )
