(function ($) {
    $(document).ready(function () {
        var table = $('#customers_id').DataTable({
            paging: true,
            pageLength: 10,
            ordering: true,
            bProcessing: false,
            columnDefs: [{
                targets: -1,
                orderable: false
            }],
            buttons: [
            'pdfHtml5',
            'excelHtml5' 
        ]
        });
        // Initialize filterTable plugin
        table.filterTable('#contact-filter');
    });
})(jQuery);