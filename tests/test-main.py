from main import greet

def test_greet_function():
    """Test the greet function"""
    result = greet("Alice")
    assert "Alice" in result
    assert "Welcome" in result
    print(f"Result: {result}")

def test_greet_with_different_names():
    """Test with different names"""
    assert "Bob" in greet("Bob")
    assert "Charlie" in greet("Charlie")
    assert "Diana" in greet("Diana")

def test_greet_format():
    """Test the exact format"""
    result = greet("Test")
    assert result == "Hello, Test! Welcome to Cyberrange."