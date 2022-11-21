## Requirements:

Language: Python
<br>Target Platform: Windows

### Task 1: Functional test suite
1.[ ] Create a fake http server in Python with API that behaves similar to https://swapi.dev/
   - [x] It should support the same three end-points (people/xx/, planets/xx/, starships/xx/)
   - [x] It can always return the same json response for any id passed.
   - [x] For some specific ids e.g. >100 should  return a 404 Not Found error with a json body that describes the problem.
   - [ ] The server should keep a log file that logs all the incoming requested URLs and response codes.
2. [ ] Create an automated test suite (using test framework like Robot Framework) that:
    - [ ] prepares the test environment by starting the http server
    - [ ] runs test cases per end-point that verify both happy path (sends back a valid json response with the expected values) or edge cases (e.g. id not found)
    - [ ] shuts down the environment
    - [ ] prints out the test execution results to the console

### Task 2: Performance test suite
- [ ] Extend the http server to incur a random small delay per http request.
- [ ] Create a performance test suite that:
    - [ ] prepares the test environment by starting the http server
    - [ ] accesses one of the end-points continuously for a time duration e.g. 1 minute (sequential access is fine)
    - [ ] for each access it keeps track of the response time on the client side
    - [ ] shuts down the environment
    - [ ] prints out mean & standard deviation of the response time for the end-point

<br> The code should be pushed to the public git repository (GitHub) and the link should be attached.

