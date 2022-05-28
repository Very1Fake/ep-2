% rebase('layout.tpl', title='Second Variant', nav_header='Second Variant', nav_link='/')

<div class="container">
    <div class="row">
        <div class="col-12 mb-4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Id deleniti natus deserunt
            optio maiores ipsa suscipit possimus praesentium. Expedita incidunt consectetur doloremque exercitationem
            alias sapiente iusto ipsum ad. Eos, ducimus!
            Praesentium voluptatum vel blanditiis minus cupiditate delectus. Voluptatum animi exercitationem asperiores
            beatae soluta laudantium doloribus aspernatur nesciunt eligendi dolorem consequatur consectetur aut a,
            magnam pariatur eos porro. Magnam, nihil eaque.
            Molestias quod alias voluptatibus? Iusto dignissimos eveniet, sequi earum accusantium at labore in similique
            assumenda praesentium, pariatur impedit? Magnam totam autem esse numquam in, magni delectus ab saepe
            architecto provident.</div>
        <div class="col-3">
            <div class="card">
                <div class="card-header">Arguments</div>
                <div class="card-body">
                    <form action="#" class="row g-3 needs-validation" novalidate>

                        <div class="col-12">
                            <label for="t2-arg" class="form-label">Running time of the queuing system</label>
                            <div class="input-group has-validation">
                                <span class="input-group-text" id="t2-arg-prepend">t<sub>2</sub></span>
                                <input type="number" class="form-control" id="t2-arg" name="numA"
                                    area-describedby="t2-arg-prepend" min="0.0001" step="0.1" value="0.5" max="1" required>
                                <div class="invalid-feedback">
                                    t<sub>2</sub> must be equal or greater than 0.5
                                </div>
                            </div>
                        </div>

                      <div class="col-12">
                            <label for="t2-arg" class="form-label">Running time of the queuing system</label>
                            <div class="input-group has-validation">
                                <span class="input-group-text" id="t2-arg-prepend">t<sub>2</sub></span>
                                <input type="number" class="form-control" id="t2-arg" name="numB"
                                    area-describedby="t2-arg-prepend" min="0.0001" step="0.1" value="0.5" max="1" required>
                                <div class="invalid-feedback">
                                    t<sub>2</sub> must be equal or greater than 0.5
                                </div>
                            </div>
                        </div>
                        
                        <div class="col-12">
                            <label for="t2-arg" class="form-label">Running time of the queuing system</label>
                            <div class="input-group has-validation">
                                <span class="input-group-text" id="t2-arg-prepend">t<sub>2</sub></span>
                                <input type="number" class="form-control" id="t2-arg" name="numC"
                                    area-describedby="t2-arg-prepend" min="0.0001" step="0.1" value="0.5" max="1" required>
                                <div class="invalid-feedback">
                                    t<sub>2</sub> must be equal or greater than 0.5
                                </div>
                            </div>
                        </div>

                        <div class="col-12">
                            <label for="t2-arg" class="form-label">Running time of the queuing system</label>
                            <div class="input-group has-validation">
                                <span class="input-group-text" id="t2-arg-prepend">t<sub>2</sub></span>
                                <input type="number" class="form-control" id="t2-arg" name="numD"
                                    area-describedby="t2-arg-prepend" min="0.0001" step="0.1" value="0.5" max="1" required>
                                <div class="invalid-feedback">
                                    t<sub>2</sub> must be equal or greater than 0.5
                                </div>
                            </div>
                        </div>

                        <div class="col-12">
                            <label for="t2-arg" class="form-label">Running time of the queuing system</label>
                            <div class="input-group has-validation">
                                <span class="input-group-text" id="t2-arg-prepend">t<sub>2</sub></span>
                                <input type="number" class="form-control" id="t2-arg" name="numE"
                                    area-describedby="t2-arg-prepend" min="0.0001" step="0.5" value="2" max="1" required>
                                <div class="invalid-feedback">
                                    t<sub>2</sub> must be equal or greater than 0.5
                                </div>
                            </div>
                        </div>

                        <div class="col-12">
                            <label for="a-arg" class="form-label">Number of requests served</label>
                            <div class="input-group has-validation">
                                <span class="input-group-text" id="a-arg-prepend">a</span>
                                <input type="number" class="form-control" id="a-arg" name="rowCount"
                                    area-describedby="a-arg-prepend" min="1" value="100" max="9999" required>
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
        <div class="col-9">
            <div class="d-flex align-items-center text-center h-100" id="no_result">
                <h3 class="display-3 w-100">No Result Yet</h3>
            </div>
            <div class="d-flex align-items-center justify-content-center h-100" id="loader_spinner" style="display: none!important;">
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
                            <th colspan="3" scope="col">Moment request was accepted</th>
                            <th colspan="2" scope="col">Counter</th>
                        </tr>
                        <tr>
                            <th>1</th>
                            <th>2</th>
                            <th>3</th>
                            <th>Serviced requests</th>
                            <th>Rejections</th>
                        </tr>
                    </thead>
                    <tbody class="table-group-divider" id="result_table_body">
                        <tr>
                            <th scope="row">1</th>
                            <td>0.31</td>
                            <td>0.31</td>
                            <td>0.312</td>
                            <td>0.312</td>
                            <td>0.312</td>
                            <td>0.312</td>
                            <td>0.312</td>
                            <td>1</td>
                            <td></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>


<script src="/static/variant_loader.js"></script>