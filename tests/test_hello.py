def test_basic_math():
    """Test that 1 + 1 = 2"""
    assert 1 + 1 == 2
    print("✅ Math works!")

def test_string():
    """Test string operations"""
    name = "Cyberrange"
    assert "Cyber" in name
    print("✅ String test passed!")

def test_list():
    """Test list operations"""
    numbers = [1, 2, 3, 4, 5]
    assert len(numbers) == 5
    assert 3 in numbers
    print("✅ List test passed!")