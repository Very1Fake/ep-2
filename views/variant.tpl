% rebase('layout.tpl', title=title, nav_header=title, nav_link=link)

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
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo reprehenderit aliquam, odit
                        recusandae magni, magnam facilis accusamus aperiam atque obcaecati non est quia molestias ut
                        libero, deleniti tenetur. Aliquam, temporibus!
                        Quas possimus id fugiat ab pariatur recusandae repudiandae nemo ipsa debitis obcaecati cumque,
                        dolore quae optio amet non totam illo. Dolore quo corporis assumenda eveniet nisi exercitationem
                        nesciunt! Culpa, tenetur.
                        Minima, atque, necessitatibus delectus sed voluptates nulla placeat amet saepe deserunt quidem,
                        natus aspernatur sequi ducimus neque sapiente voluptas harum repellendus animi eos perferendis
                        mollitia. Accusantium reprehenderit sit iure alias!
                        Ad, soluta! Et quo ut amet eligendi error quis laboriosam inventore quisquam, eum culpa minima,
                        libero illo nam rerum unde rem? Dolores molestiae, sed odit sapiente corporis ducimus tempore
                        quo?
                        Quod corporis eius molestias consequuntur unde, nulla sint ipsum, eligendi maiores fugit at
                        rerum deserunt repellat maxime aliquam minus beatae nam, impedit laudantium eos placeat. Culpa
                        vel facere vero praesentium?
                    </div>
                </div>
            </div>
        </div>
        <div class="col-12">
            <div class="row gy-3">
                <div class="col-12">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Id deleniti natus deserunt
                    optio maiores ipsa suscipit possimus praesentium. Expedita incidunt consectetur doloremque
                    exercitationem
                    alias sapiente iusto ipsum ad. Eos, ducimus!
                    Praesentium voluptatum vel blanditiis minus cupiditate delectus. Voluptatum animi exercitationem
                    asperiores
                    beatae soluta laudantium doloribus aspernatur nesciunt eligendi dolorem consequatur consectetur aut
                    a,
                    magnam pariatur eos porro. Magnam, nihil eaque.
                    Molestias quod alias voluptatibus? Iusto dignissimos eveniet, sequi earum accusantium at labore in
                    similique
                    assumenda praesentium, pariatur impedit? Magnam totam autem esse numquam in, magni delectus ab saepe
                    architecto provident.
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
                    <thead>
                        <tr>
                            <th rowspan="2" scope="col">Request num.</th>
                            <th rowspan="2" scope="col">Rand. num. r<sub>i</sub></th>
                            <th rowspan="2" scope="col">-ln r<sub>i.</sub></th>
                            <th rowspan="2" scope="col">Time between two consecutive requests</th>
                            <th rowspan="2" scope="col">Moment of receipt of the request</th>
                            % if variant == 2:
                            <th colspan="3" scope="col">Moment request was accepted</th>
                            % end
                            % if variant == 3:
                            <th colspan="4" scope="col">Moment request was accepted</th>
                            % end
                            <th colspan="2" scope="col">Counter</th>
                        </tr>
                        <tr>
                            <th>1</th>
                            <th>2</th>
                            <th>3</th>
                            % if variant == 3:
                            <th>4</th>
                            % end
                            <th>Serviced requests</th>
                            <th>Rejections</th>
                        </tr>
                    </thead>
                    <tbody class="table-group-divider" id="result_table_body">
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>


<script src="/static/variant_loader.js"></script>