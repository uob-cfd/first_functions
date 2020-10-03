test = {
  'name': 'Question 5_1_count_4_girls',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You haven't defined a count_4_girls function yet
          >>> 'count_4_girls' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # count_4_girls is not a function
          >>> import types
          >>> type(count_4_girls) is types.FunctionType
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 0 <= count_4_girls() <= 4
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          # counts = np.random.binomial(4, 0.487, (10000, 1000))
          # means = np.mean(counts, axis=0)
          # np.min(means), np.max(means)
          'code': r"""
          >>> counts = np.zeros(10000)
          >>> for i in range(10000):
          ...     counts[i] = count_4_girls()
          >>> np.all(counts >= 0)
          True
          >>> np.all(counts <= 4)
          True
          >>> 1.9 <= np.mean(counts) <= 1.99
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
