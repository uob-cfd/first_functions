test = {
  'name': 'Question 5_2_count_girls',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You haven't defined a count_girls function yet
          >>> 'count_girls' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # count_girls is not a function
          >>> import types
          >>> type(count_girls) is types.FunctionType
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 0 <= count_girls(2, 0.5) <= 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          # counts = np.random.binomial(6, 0.3, (10000, 1000))
          # means = np.mean(counts, axis=0)
          # np.min(means), np.max(means)
          'code': r"""
          >>> counts = np.zeros(10000)
          >>> for i in range(10000):
          ...     counts[i] = count_girls(6, 0.3)
          >>> np.all(counts >= 0)
          True
          >>> np.all(counts <= 6)
          True
          >>> 1.75 <= np.mean(counts) <= 1.84
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          # counts = np.random.binomial(12, 0.7, (10000, 1000))
          # means = np.mean(counts, axis=0)
          # np.min(means), np.max(means)
          'code': r"""
          >>> counts = np.zeros(10000)
          >>> for i in range(10000):
          ...     counts[i] = count_girls(12, 0.7)
          >>> np.all(counts >= 0)
          True
          >>> np.all(counts <= 12)
          True
          >>> 8.3 <= np.mean(counts) <= 8.46
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
