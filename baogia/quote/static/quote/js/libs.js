function get_csrfmiddlewaretoken() {
	return $(".no-s").attr('val');
}

function show_mess(mess){
    toastr.success(mess);
}