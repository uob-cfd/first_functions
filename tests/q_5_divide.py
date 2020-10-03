test = {
  'name': 'Question 5_divide',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Oh dear - the function is returning None!
          >>> divide(10, 2) is not None
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> divide(10, 2)
          5.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> divide(4, 2)
          2.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> divide(25, 4)
          6.25
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
