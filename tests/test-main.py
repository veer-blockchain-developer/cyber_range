from main import greet

def test_greet_function():
    """Test the greet function"""
    result = greet("Alice")
    assert "Alice" in result
    assert "Welcome" in result

def test_greet_with_emoji():
    """Test that emoji is included"""
    result = greet("Bob")
    assert "🚀" in result

def test_greet_empty_name():
    """Test with empty name"""
    result = greet("")
    assert result == "Hello there!"