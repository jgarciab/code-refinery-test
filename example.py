def better_round(a):
	return round(a)


def test_better_round():
	assert better_round(9.5) == 10
	assert better_round(8.5) == 9