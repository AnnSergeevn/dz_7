import pytest

def find_elem(st):
    cicle_st_close = st.count("(")
    cicle_st_open = st.count(")")
    square_st_close = st.count("[")
    square_st_open = st.count("]")
    curly_st_close = st.count("{")
    curly_st_open = st.count("}")

    if curly_st_open == curly_st_close and cicle_st_close == cicle_st_open and square_st_open == square_st_close:
        print("Сбалансированно")
        return True
    else:
        print("Несбалансированно")
        return False


def test_find_elem():
    s = "(((([{}]))))"
    s1 = "[((([[[]]])))]"
    s2 = "{{[(])]}}"
    assert find_elem(s) == True
    assert find_elem(s1) == True
    assert find_elem(s2) == False


if __name__ == '__main__':
    s = "(((([{}]))))"
    s1 = "[((([[[]]])))]"
    s2 = "{{[(])]}}"
    find_elem(s)
    find_elem(s1)
    find_elem(s2)
    test_find_elem()