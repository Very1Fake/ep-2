(() => {
    'use strict'

    const forms = document.querySelectorAll('.needs-validation');
    const button = document.getElementById('btn_submit');
    const spinner = document.getElementById('loader_spinner');
    const no_result = document.getElementById('no_result');
    const table = document.getElementById('result_table');
    const table_body = document.getElementById('result_table_body');

    function setStateToLoading() {
        console.debug('State set to loading');
        button.disabled = true;
        spinner.style.display = null;
        table.hidden = true;
    }

    function setStateToResult() {
        console.debug('State set to result');
        button.disabled = false;
        spinner.style.setProperty('display', 'none', 'important');
        table.hidden = false;
    }

    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            let is_checked = form.checkValidity();
            form.classList.add('was-validated');
            event.preventDefault()
            event.stopPropagation()

            if (is_checked) {
                no_result.style.setProperty('display', 'none', 'important');
                setStateToLoading();
                fetch('/api/second_variant', {
                    method: 'POST',
                    body: new FormData(form),
                    mode: 'cors',
                    credentials: 'same-origin',
                }).then((response) => {
                    if (response.ok) {
                        console.log("Success");
                        return response.json();
                    } else {
                        console.error("Request Failed");
                        setStateToResult(); // TODO: Error state
                    }
                }).then((json) => {
                    console.log(json);

                    if ('ok' in json) {
                        let result = json['ok'];
                        table_body.innerHTML = '';

                        result.forEach(row => {
                            function table_row() {
                                let tr = document.createElement('tr');
                                let th = document.createElement('th');
                                th.setAttribute('scope', 'row');
                                th.innerHTML = row[0];
                                tr.appendChild(th);

                                row.slice(1, 10).forEach(str => {
                                    var td = document.createElement('td');
                                    td.innerHTML = str;
                                    tr.appendChild(td);
                                });

                                return tr;
                            }

                            table_body.appendChild(table_row());
                        });
                        form.classList.remove('was-validated');
                    } else if ('error' in json) {
                        console.error("Bad Result");
                    } else {
                        console.error("Invalid format");
                    }

                    setStateToResult();
                })
            }

        }, false)
    })
})()