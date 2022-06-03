(() => {
    'use strict'

    // Get element object
    const forms = document.querySelectorAll('.needs-validation');
    const target = document.getElementById('target');
    const button = document.getElementById('btn_submit');
    const spinner = document.getElementById('loader_spinner');
    const no_result = document.getElementById('no_result');
    const error_view = document.getElementById('error_view');
    const error_header = document.getElementById('error_header');
    const error_message = document.getElementById('error_message');
    const table = document.getElementById('result_table');
    const table_body = document.getElementById('result_table_body');

    // Switch state to show lading spinner
    function setStateToLoading() {
        console.debug('State set to loading');
        button.disabled = true;
        spinner.style.display = null;
        error_view.style.setProperty('display', 'none', 'important');
        table.hidden = true;
    }

    // Switch state to show error
    function setStateToError(header, message) {
        console.debug('State set to result');
        button.disabled = false;
        spinner.style.setProperty('display', 'none', 'important');
        error_view.style.display = null;
        error_header.innerHTML = header;
        error_message.innerHTML = message;
        table.hidden = true;
    }

    // Switch state to show results
    function setStateToResult() {
        console.debug('State set to result');
        button.disabled = false;
        spinner.style.setProperty('display', 'none', 'important');
        error_view.style.setProperty('display', 'none', 'important');
        table.hidden = false;
    }

    // Event handler to form
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            let is_checked = form.checkValidity();
            form.classList.add('was-validated');
            event.preventDefault()
            event.stopPropagation()

            // Form validation
            if (is_checked) {
                no_result.style.setProperty('display', 'none', 'important');
                setStateToLoading();

                // XHR request
                fetch(target.value, {
                    method: 'POST',
                    body: new FormData(form),
                    mode: 'cors',
                    credentials: 'same-origin',
                }).then(async response => {
                    const isJson = response.headers.get('content-type')?.includes('application/json');
                    const data = isJson ? await response.json() : null;

                    if (response.ok) {
                        console.log("Success");
                        console.log(data);

                        if ('ok' in data) {
                            console.log("ok");
                            let result = data['ok'];
                            table_body.innerHTML = '';

                            // Table filling code
                            result.forEach(row => {
                                function table_row() {
                                    let tr = document.createElement('tr');
                                    let th = document.createElement('th');
                                    th.setAttribute('scope', 'row');
                                    th.innerHTML = row[0];
                                    tr.appendChild(th);

                                    row.slice(1, row.length).forEach(str => {
                                        var td = document.createElement('td');
                                        td.innerHTML = str;
                                        tr.appendChild(td);
                                    });

                                    return tr;
                                }

                                table_body.appendChild(table_row());
                            });
                            form.classList.remove('was-validated');

                            setStateToResult();
                        } else if ('error' in data) {
                            // Server error handling
                            console.log("err");
                            setStateToError("Bad Result", data['error']);
                        } else {
                            // Format error handling
                            console.log("none");
                            setStateToError("Invalid format", 'Response has neither "ok" nor "error" field');
                        }
                    } else {
                        // Request error handling
                        console.error("Request Failed");
                        return Promise.reject((data && data.message) || response.status);
                    }
                }).catch(error => {
                    // Switch state to error
                    console.error("Request Failed");
                    setStateToError("Request Failed", error);
                });
            }

        }, false)
    })
})()