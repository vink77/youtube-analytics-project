from src.video import Video, PLVideo

@pytest.fixture
def chanV():
    return Video("AWX4JnAnjBE")
def test_str():
    video1 = Video("AWX4JnAnjBE")
    video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')

    assert str(chanV) == 'GIL в Python: зачем он нужен и как с этим жить'
    assert str(video2) == 'MoscowPython Meetup 78 - вступление'

