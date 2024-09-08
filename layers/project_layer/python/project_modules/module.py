from result import Result, Ok


def example_function() -> Result[str, Exception]:
    return Ok("printing from layer")
