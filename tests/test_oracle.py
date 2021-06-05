def test_direct_import():
    """Check calling function after direct import"""
    from cython_oracle.oracle import answer_to_all_questions

    assert answer_to_all_questions() == 42


def test_parent_module_import():
    """Check calling function after import of parent module"""
    from cython_oracle import oracle

    assert oracle.answer_to_all_questions() == 42


def test_root_module_import():
    """Check calling function after import of root module"""
    import cython_oracle

    assert cython_oracle.oracle.answer_to_all_questions() == 42
