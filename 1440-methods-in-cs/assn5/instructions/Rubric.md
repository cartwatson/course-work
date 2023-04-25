# CS 1440 Assignment 5 Rubric

| Points | Criteria
|:------:|-----------------------------------------------------------------------------------------------------------
| 10     | Program accepts *only* absolute URLs from the command-line<br/>Relative URLs are rejected with an error message
|  5     | Maximum recursion depth can be overridden from command line<br/>By default the maximum recursion depth is limited to 3 levels<br/>When this parameter is not supplied or is not a positive integer default to a depth of `3` links
|  5     | `crawl()` is written such that it does not rely on global variables for correct functioning
|  5     | Current recursion depth is accurately maintained and correctly updated
| 10     | Visited URLs are printed to the screen<br/>Recursion Depth is indicated in program output by indenting with four spaces per level<br/>Unvisited URLs are **NOT** printed
|  5     | Visited URLs are recorded in a set and are not re-visited (or redisplayed)
|  5     | Relative URLs are converted to absolute URLs
|  5     | URL fragments are stripped before sites are visited and before they are stored in the visited set to prevent double-visiting
| 10     | Exception Handling protects program from crashing when encountering uncooperative sites<br/>Catch exceptions, display an error message, and continue on to the next URL<br/>Getting hung up (or freezing) on some websites is *not* penalized.
| 15     | `crawl()` is recursively called from within itself up to `maxdepth` calls deep<br/>Base case(s) prevent unbounded recursive calls

**Total points: 75**


## Penalties

*   **75 point penalty** if you submit the starter code **unchanged**.
*   This assignment is *not* eligible for the grading gift.  This due date cannot be moved.
*   Review the Course Rules document to avoid general penalties which apply to all assignments.
    *   **10 point penalty** Pay attention to the name you give your repository on GitLab.
    *   **10 point penalty per file** Don't forget to include your *Software Development Plan* and *Sprint Signature* documents in the `doc/` directory.
    *   Verify your submission on GitLab.  Clone your repo to a new location and test it there to ensure that it is complete and correct.
*   Use only the libraries named in the [Instructions](Instructions.md).  If your code imports a library which your grader doesn't happen to have installed on that computer the resulting `ModuleNotFoundError` will be treated as a crash and penalized at 50% of the assignment's value.
