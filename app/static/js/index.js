var dataTableElement;
var dataTableUrl = "http://localhost:8000/api/read_csv"
window.addEventListener('load', (e) => {
    $.ajax({
        url: 'http://localhost:8000/app/data_columns',
        success: function (data) {
            let selector = document.getElementById("choose_key")
            for (const key in data.table_columns) {
                let option = document.createElement('option')
                option.value = data.table_columns[key];
                option.innerHTML = key;
                selector.append(option)
            }
        }
    });
})

function reloadDataTable(newUrl) {
    // Change the AJAX URL
    dataTableElement.ajax.url(newUrl).load();
}
// Initialize the DataTable
$(document).ready(function () {
    dataTableElement = $('#data_table').DataTable({
        ajax: dataTableUrl,
        columns: [
            {
                "data": "leg"
            },
            {
                "data": "tta"
            },
            {
                "data": "uuid"
            },
            {
                "data": "pdd_ms"
            },
            {
                "data": "billsec"
            },
            {
                "data": "billmsec"
            },
            {
                "data": "duration"
            },
            {
                "data": "direction"
            },
            {
                "data": "accountcode"
            },
            {
                "data": "bridge_uuid"
            },
            {
                "data": "domain_uuid"
            },
            {
                "data": "record_name"
            },
            {
                "data": "record_path"
            },
            {
                "data": "start_epoch"
            },
            {
                "data": "start_stamp"
            },
            {
                "data": "answer_stamp"
            },
            {
                "data": "hangup_cause"
            },
            {
                "data": "source_number"
            },
            {
                "data": "caller_id_name"
            },
            {
                "data": "raw_data_exists"
            },
            {
                "data": "caller_id_number"
            },
            {
                "data": "rtp_audio_in_mos"
            },
            {
                "data": "caller_destination"
            },
            {
                "data": "destination_number"
            },
            {
                "data": "sip_hangup_disposition"
            }
        ]
    });
});

$('#custom_search_by_key').on("keyup", (elem) => {
    let selectedVaal = document.getElementById("choose_key")
    var searchValue = elem.target.value;
    let newUrl = dataTableUrl + `?${selectedVaal.value}=${searchValue}`
    reloadDataTable(newUrl)
})
