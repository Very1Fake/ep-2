% rebase('layout.tpl', title=title)
% include('navbar.tpl', nav_header=title, nav_link=link)

% if variant == 1:
<input type="hidden" id="target" value="/api/first_variant">
% end
% if variant == 2:
<input type="hidden" id="target" value="/api/second_variant">
% end
% if variant == 3:
<input type="hidden" id="target" value="/api/third_variant">
% end

<div class="container">
    <div class="row gy-3">
        <div class="modal modal-lg fade" id="theoryModal" data-bs-keyboard="false" tabindex="-1"
            aria-labelledby="theoryModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="theoryModalLabel">Variant Theory</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        % if variant == 1:
                        <p>
                            The system consists of two blocks connected in series.
                            The system fails when at least one block fails. The first block contains
                            two elements: A, B (they are connected in parallel) and fails when both
                            elements fail simultaneously. The second one contains one element
                            with and fails when this element fails.
                        </p>
                        <p>
                            a) Find by the Monte Carlo method an estimate of P*
                            reliability (probability of failure-free operation)
                            of the system, knowing the probability of failure-free operation
                            of the elements: P(A)= 0.8, P (B)=0.85, P (C)= 0.6;
                        </p>
                        <p>
                            b) find the absolute error |P−P*| of the found value, where P
                            is the reliability of the system, calculated analytically.
                            Perform 50 tests.
                        </p>
                        <p>
                            Solution:
                        </p>
                        <p>
                            Using a random number generator, we obtain
                            (or select from special tables of uniformly distributed random numbers)
                            three random numbers, for example: 0.10, 0.09 and 0.73; then we consider
                            that if the random number is less than the probability of the corresponding event,
                            then the event has occurred (the element works flawlessly); if the random number
                            is greater than or equal to the probability of the event, then the event has not
                            occurred (failure).
                        </p>
                        <p>
                            We will play out events A, B, C, consisting in the trouble-free operation
                            of elements A, B, C, respectively. The test results will be recorded in the
                            calculation table. Since P(A) = 0.8 and 0.10 &#60;0.8, the event has occurred,
                            i.e. element A in this test works flawlessly. Since P(B)=0.85 and 0.09&#60;0.85,
                            event B has occurred, i.e. element B works flawlessly.
                        <p>
                            Thus, both elements of the first block work; therefore, the first block itself
                            works. In the corresponding cells of Table 1, we put a plus sign (or 1).
                        </p>
                        <p>
                            Since P(S)=0.6 and 0.73&#62;0.6, then event C has not occurred, i.e. element
                            C is rejected; in other words, the second block, and hence the entire system,
                            is rejected. In the corresponding cells of Table 1, we put a minus sign (or 0).
                        </p>
                        <p>
                            The other tests are played out in the same way. Table 1 shows the results
                            of four tests.
                        </p>
                        <img src="/static/images/first_variant_table.png" class="img-fluid rounded my-4 px-3" alt="...">
                        <p>
                            After performing 50 tests, we get that in 28 of them the system worked flawlessly.
                            As an estimate of the desired reliability P, we will take the relative frequency
                            P* = 28/50 = 0.56.
                        </p>
                        <p>
                            b) We will find the reliability of the system P analytically.
                            The probabilities of failure-free operation of the first and
                            second blocks are equal, respectively:
                        </p>
                        <p>
                            P<sub>1</sub>= 1-P(B&#773;)∙P(A&#773;) = 1-0.2∙0.15 = 0.97, P<sub>2</sub> = P(C) = 0.6
                        </p>
                        <p>
                            The probability of failure-free operation of the system
                        </p>
                        <p>
                            P = P<sub>1</sub>∙P<sub>2</sub> = 0.97∙0.6=0.582
                        </p>
                        <p>
                            The required absolute error is equal to |P−P*| = 0.582−0.56 = 0.022.
                        </p>
                        % end
                        % if variant == 2 or variant == 3:
                        <p>
                            A Poisson flow of requests enters a three-channel queuing system with a failure. The time
                            between receipts of two consecutive applications is distributed according to the exponential
                            law f(τ)=5e<sup>-5τ</sup>
                        </p>
                        <p>
                            Solution:
                        </p>
                        <p>
                            Let Т<sub>1</sub>=0 be the moment of receipt of the first request. The application will go
                            to the first channel and will be served by it. The moment of the end of servicing the first
                            request Т<sub>1</sub>+0.5=0+0.5=0.5. We write one in the counter of serviced requests.
                        </p>
                        <p>
                            We will find the moments of receipt of subsequent requests by the formula Т<sub>i</sub>=
                            Т<sub>i-1</sub>+τ i, where τ<sub>i</sub> - is the duration of time between two consecutive
                            orders with numbers i-1 and i.
                        </p>
                        <p>
                            Considering that, by condition, λ=5, we get τ = −0.2 ln r<sub>i</sub>.
                        </p>
                        <p>
                            Random numbers r<sub>i</sub> are generated using a random number generator. Let the time
                            between arrivals of the first and second applications be a random number equal to
                            r<sub>1</sub>=0.10. Then τ<sub>2</sub>=−0.2∙ln(0.10)=0.460 The first request arrived at the
                            Т<sub>1</sub>=0 Therefore, the second application arrived at the time
                            T<sub>2</sub>=T<sub>1</sub>+0.460=0+0.460=0.460 At this moment, the first channel is still
                            busy servicing the first request, so the second request will go to the second one and be
                            served by it. The moment of the end of servicing the second request is
                            T<sub>2</sub>+0.5=0.460+0.5=0.960. To the counter of serviced applications in doses. For the
                            next random number r<sub>2</sub>=0.09, we will play the time τ<sub>3</sub> between the
                            arrival of the second and third requests: τ<sub>3</sub>=−0.2∙ln(0.09)=0.2∙2.41=0.482.
                        </p>
                        <p>
                            The second request was received at the moment T<sub>2</sub>=0.460. Therefore, the third
                            order was received at the moment T<sub>3</sub>=T<sub>2</sub>+0.482=0.460+0.482=0.942. At
                            this moment, the first channel is already free, and the third request will go to the first
                            channel. The moment of the end of servicing the third request is
                            T<sub>3</sub>+0.5=0.942+0.5=1.442. Add one to the counter of serviced requests. Further
                            calculation is carried out similarly, moreover, if at the time of receipt of the application
                            all channels are busy (the moment of receipt of the application is less than each of the
                            moments of the end of service), then one is added to the failure counter.
                        </p>
                        <p>
                            Note that the service of the 20th claim will end at time 4.148>4, so this claim is rejected.
                            The test is terminated (in the table, "stop" is written) if the moment of receipt of the
                            application is T>4.
                        </p>
                        <img src="/static/images/kelmytable.png" class="img-fluid rounded my-4 px-3" alt="...">
                        <p>
                            From the table we find that in 4 minutes a total of 20 applications were received; served
                            x<sub>1</sub> =12. We perform five more tests in the same way, we get:
                            x<sub>2</sub>=15, x<sub>3</sub>=14, x<sub>4</sub>=12, x<sub>5</sub>=13, x<sub>6</sub>=15.
                            As an estimate of the desired mathematical expectation a - the number of serviced requests,
                            we take the sample mean: a=vinculum(x)=(2∙12+13+14+2∙15)/6=13.5.
                        </p>
                        % end
                    </div>
                </div>
            </div>
        </div>
        <div class="col-12">
            <div class="row gy-3">
                <div class="col-12">
                    % if variant == 1:
                    The system consists of two blocks connected in series. The system fails if at least one block fails.
                    The first block contains three elements: A, B, C, and the second - two elements: D, E. The elements
                    of each block are connected in parallel. The block fails when all the elements included in it fail
                    simultaneously. The probabilities of failure-free operation of elements P(A), P(B), P(C), P(D), P(E)
                    are entered by the user.
                    % end
                    % if variant == 2:
                    A Poisson flow of requests enters a three-channel queuing system with a failure. The time between
                    receipts of two consecutive applications is distributed according to the exponential law
                    f(τ)=αe<sup>-ατ</sup>. The duration of servicing each request is 0.5 min. Find by the Monte Carlo
                    method the mathematical expectation a of the number of serviced requests for the time T=4 min.
                    % end
                    % if variant == 3:
                    A Poisson flow of requests enters a four-channel queuing system with an unlimited queue. The time
                    between receipts of two consecutive applications is distributed according to the exponential law
                    f(τ)=αe<sup>-ατ</sup>. The service time for each request is t1 min. Find by the Monte Carlo method
                    the mathematical expectation a of the number of serviced requests for the time T=t2 hours.
                    The values t1, t2 and α are set by the user.
                    % end
                </div>
                <div class="offset-md-10 col-md-2 col-sm-12">
                    <button type="button" class="btn btn-outline-primary btn-sm w-100" data-bs-toggle="modal"
                        data-bs-target="#theoryModal">Read theory</button>
                </div>
            </div>
        </div>
        <div class="col-xl-3 col-sm-12">
            <div class="card">
                <div class="card-header">Arguments</div>
                <div class="card-body">
                    <form action="#" class="row g-3 needs-validation" novalidate>
                        % if variant == 2 or variant == 3:
                        <div class="col-12">
                            <label for="t1-arg" class="form-label">The duration of each request</label>
                            <div class="input-group has-validation">
                                <span class="input-group-text" id="t1-arg-prepend">t<sub>1</sub></span>
                                <input type="number" class="form-control" id="t1-arg" name="t1"
                                    area-describedby="t1-arg-prepend" min="0.1" step="0.1" value="0.5" required>
                                <div class="invalid-feedback">
                                    t<sub>1</sub> must be equal or greater than 0.1
                                </div>
                            </div>
                        </div>
                        <div class="col-12">
                            <label for="t2-arg" class="form-label">Running time of the queuing system</label>
                            <div class="input-group has-validation">
                                <span class="input-group-text" id="t2-arg-prepend">t<sub>2</sub></span>
                                <input type="number" class="form-control" id="t2-arg" name="t2"
                                    area-describedby="t2-arg-prepend" min="0.5" step="0.5" value="2" required>
                                <div class="invalid-feedback">
                                    t<sub>2</sub> must be equal or greater than 0.5
                                </div>
                            </div>
                        </div>
                        <div class="col-12">
                            <label for="a-arg" class="form-label">Number of requests served</label>
                            <div class="input-group has-validation">
                                <span class="input-group-text" id="a-arg-prepend">a</span>
                                <input type="number" class="form-control" id="a-arg" name="a"
                                    area-describedby="a-arg-prepend" min="1" value="25" required>
                                <div class="invalid-feedback">
                                    a must be greater than 1
                                </div>
                            </div>
                        </div>
                        % end

                        % if variant == 1:
                        <div class="col-12">
                            <label for="numA-arg" class="form-label">Probabilities of failure-free operation of element
                                A of the first module</label>
                            <div class="input-group has-validation">
                                <span class="input-group-text" id="numA-arg-prepend">P(A)</span>
                                <input type="number" class="form-control" id="numA-arg" name="numA"
                                    area-describedby="numA-arg-prepend" min="0.0001" step="0.0001" value="0.5" max="1"
                                    required>
                                <div class="invalid-feedback">
                                    P(A) must be &ge;0.0001 or &le;1 </div>
                            </div>
                        </div>

                        <div class="col-12">
                            <label for="numB-arg" class="form-label">Probabilities of failure-free operation of
                                element B of the first module</label>
                            <div class="input-group has-validation">
                                <span class="input-group-text" id="numB-arg-prepend">P(B)</span>
                                <input type="number" class="form-control" id="numB-arg" name="numB"
                                    area-describedby="numB-arg-prepend" min="0.0001" step="0.0001" value="0.5" max="1"
                                    required>
                                <div class="invalid-feedback">
                                    P(B) must be &ge;0.0001 or &le;1 </div>
                            </div>
                        </div>

                        <div class="col-12">
                            <label for="numC-arg" class="form-label">Probabilities of failure-free operation of
                                element C of the first module</label>
                            <div class="input-group has-validation">
                                <span class="input-group-text" id="numC-arg-prepend">P(C)</span>
                                <input type="number" class="form-control" id="numC-arg" name="numC"
                                    area-describedby="numC-arg-prepend" min="0.0001" step="0.0001" value="0.5" max="1"
                                    required>
                                <div class="invalid-feedback">
                                    P(C) must be &ge;0.0001 or &le;1 </div>
                            </div>
                        </div>

                        <div class="col-12">
                            <label for="numD-arg" class="form-label">Probabilities of failure-free operation
                                of element D of the second module</label>
                            <div class="input-group has-validation">
                                <span class="input-group-text" id="numD-arg-prepend">P(D)</span>
                                <input type="number" class="form-control" id="numD-arg" name="numD"
                                    area-describedby="numD-arg-prepend" min="0.0001" step="0.0001" value="0.5" max="1"
                                    required>
                                <div class="invalid-feedback">
                                    P(D) must be &ge;0.0001 or &le;1 </div>
                            </div>
                        </div>

                        <div class="col-12">
                            <label for="numE-arg" class="form-label">Probabilities of failure-free
                                operation of element E of the second module</label>
                            <div class="input-group has-validation">
                                <span class="input-group-text" id="numE-arg-prepend">P(E)</span>
                                <input type="number" class="form-control" id="numE-arg" name="numE"
                                    area-describedby="numE-arg-prepend" min="0.0001" step="0.0001" value="0.5" max="1"
                                    required>
                                <div class="invalid-feedback">
                                    P(E) must be &ge;0.0001 or &le;1 </div>
                            </div>
                        </div>

                        <div class="col-12">
                            <label for="rowCount-arg" class="form-label">Number of tests</label>
                            <div class="input-group has-validation">
                                <span class="input-group-text" id="rowCount-arg-prepend">Tests</span>
                                <input type="number" class="form-control" id="rowCount-arg" name="rowCount"
                                    area-describedby="rowCount-arg-prepend" min="1" value="100" max="9999" required>
                                <div class="invalid-feedback">
                                    Tests number must be &ge;1 or &le;9999 </div>
                            </div>
                        </div>
                        % end

                        <div class="col-12">
                            <button class="btn btn-primary mt-3 w-100" type="submit" id="btn_submit">Submit</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
        <div class="col-xl-9 col-sm-12 mb-3">
            <div class="d-flex align-items-center text-center h-100" id="no_result">
                <h3 class="display-3 w-100">No Result Yet</h3>
            </div>
            <div class="row h-100 align-items-center" id="error_view" style="display: none!important;">
                <div class="col"></div>
                <div class="col-6">
                    <div class="card text-bg-danger mb-3">
                        <div class="card-header" id="error_header">Request failed</div>
                        <div class="card-body">
                            <h5 class="card-title">Error message:</h5>
                            <p class="card-text" id="error_message">Some error message.</p>
                        </div>
                    </div>
                </div>
                <div class="col"></div>
            </div>
            <div class="d-flex align-items-center justify-content-center h-100" id="loader_spinner"
                style="display: none!important;">
                <div class="spinner-border spinner-style text-secondary" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
            </div>
            <div class="table-responsive" id="result_table" hidden>
                <table class="table table-striped table-bordered text-center">
                    % if variant == 1:
                    <tr>
                        <th rowspan="3" scope="col">Number of test</th>
                        <th rowspan="3" scope="col">Blocks</th>
                        <th rowspan="2" colspan="5" scope="col">Random numbers, modeling elements</th>
                        <th colspan="7" scope="col">Conclusion about the work</th>
                    </tr>
                    <tr>
                        <th colspan="5" scope="col">elements</th>
                        <th rowspan="2" scope="col">blocks</th>
                        <th rowspan="2" scope="col">system</th>
                    </tr>
                    <tr>
                        <th>A</th>
                        <th>B</th>
                        <th>C</th>
                        <th>D</th>
                        <th>E</th>
                        <th>A</th>
                        <th>B</th>
                        <th>C</th>
                        <th>D</th>
                        <th>E</th>
                    </tr>
                    % end
                    % if variant == 2 or variant == 3:
                    <tr>
                        <th rowspan="2" scope="col">Request num.</th>
                        <th rowspan="2" scope="col">Rand. num. r<sub>i</sub></th>
                        <th rowspan="2" scope="col">-ln r<sub>i.</sub></th>
                        <th rowspan="2" scope="col">Time between two consecutive requests</th>
                        <th rowspan="2" scope="col">Moment of receipt of the request</th>
                        % if variant == 2:
                        <th colspan="3" scope="col">Moment request will be processed</th>
                        <th colspan="2" scope="col">Counter</th>
                        % end
                        % if variant == 3:
                        <th colspan="4" scope="col">Moment request will be processed</th>
                        <th rowspan="2" scope="col">Serviced requests</th>
                        % end
                    </tr>
                    <tr>
                        <th>1</th>
                        <th>2</th>
                        <th>3</th>
                        % if variant == 3:
                        <th>4</th>
                        % end
                        % if variant == 2:
                        <th>Serviced requests</th>
                        <th>Rejections</th>
                        % end
                    </tr>
                    % end
                    <tbody class="table-group-divider" id="result_table_body">
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>


<script src="/static/variant_loader.js"></script>