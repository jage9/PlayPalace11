from buffer_system import BufferSystem


def test_add_item_populates_buffer_and_all():
    buffers = BufferSystem()
    buffers.create_buffer("all")
    buffers.create_buffer("activity")

    buffers.add_item("activity", "joined table")

    assert buffers.buffers["activity"][0]["text"] == "joined table"
    assert buffers.buffers["all"][0]["text"] == "joined table"
    assert buffers.buffer_positions["activity"] == 0


def test_navigation_updates_current_buffer():
    buffers = BufferSystem()
    buffers.create_buffer("all")
    buffers.create_buffer("activity")
    buffers.create_buffer("chat")

    assert buffers.get_current_buffer_name() == "all"
    buffers.next_buffer()
    assert buffers.get_current_buffer_name() == "activity"
    buffers.next_buffer()
    buffers.next_buffer()  # should clamp at last buffer
    assert buffers.get_current_buffer_name() == "chat"
    buffers.previous_buffer()
    assert buffers.get_current_buffer_name() == "activity"
    buffers.first_buffer()
    assert buffers.get_current_buffer_name() == "all"
    buffers.last_buffer()
    assert buffers.get_current_buffer_name() == "chat"


def test_move_in_buffer_traverses_messages():
    buffers = BufferSystem()
    buffers.create_buffer("all")
    buffers.create_buffer("activity")
    for i in range(3):
        buffers.add_item("activity", f"msg-{i}")
    buffers.last_buffer()
    # Default position is newest message index 0
    assert buffers.get_current_item()["text"] == "msg-2"
    buffers.move_in_buffer("older")
    assert buffers.get_current_item()["text"] == "msg-1"
    buffers.move_in_buffer("oldest")
    assert buffers.get_current_item()["text"] == "msg-0"
    buffers.move_in_buffer("newest")
    assert buffers.get_current_item()["text"] == "msg-2"


def test_toggle_mute_and_get_muted_buffers():
    buffers = BufferSystem()
    buffers.create_buffer("activity")
    assert buffers.is_muted("activity") is False
    buffers.toggle_mute("activity")
    assert buffers.is_muted("activity") is True
    assert "activity" in buffers.get_muted_buffers()
    buffers.toggle_mute("activity")
    assert buffers.is_muted("activity") is False


def test_clear_buffer_and_all_buffers():
    buffers = BufferSystem()
    buffers.create_buffer("all")
    buffers.create_buffer("activity")
    buffers.add_item("activity", "first")
    buffers.clear_buffer("activity")
    assert buffers.buffers["activity"] == []
    assert buffers.buffer_positions["activity"] == 0

    buffers.add_item("activity", "second")
    buffers.add_item("activity", "third")
    buffers.clear_all_buffers()
    assert all(not buf for buf in buffers.buffers.values())
