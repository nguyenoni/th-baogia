
function show_mess(mess){
    toastr.success(mess);
}
// when select product
    $('select.product').change(function (e) {

        // e.stopImmediatePropagation();
        e.preventDefault();
         let selected = $(this).children("option:selected").val()
        //  $district = $('select.district')
        //  $district.children().remove()
        //  $district.append($.parseHTML("<option value=''>-- Chọn Quận/Huyện--</option>"));
 
        //  $project = $('select.project')
        //  $project.children().remove()
        //  $project.append($.parseHTML("<option value='0'>-- Chọn Dự Án--</option>"));
 
         dt = {
             'unique_product': selected,
             'csrfmiddlewaretoken': get_csrfmiddlewaretoken(),
         }
         $.ajax({
            type: 'POST',
            url: 'api/load-volume-product/',
            dataType: 'json',
            data: dt,
            success: function(data){
                if(data.data.status==200){
                    show_mess(data.data.message)
                    arr_dt = data.data.data
                    $volume = $('select.volume')
                    $volume.children().remove();
                    $volume.append($.parseHTML(`<option value="">--Chọn dung tích--</option>`))
                    arr_dt.map(item=>{
                        $volume.append($.parseHTML(`<option value="${item.unique_volume}">${item.name}</option>`))
                    })
                    // $('#nof').removeClass('hidden')
                    // $('#nof>strong').text(data.message)
                    // $('#comment').val('')
                }
                else{
                    show_mess(data.data.message)
                }


            }


        })
    })

// when select volume
$('select.volume').change(function(e){
    console.log('a')
    // e.preventDefault();
    let valv = $(this).children("option:selected").val();
    let valp = $('select.product').children("option:selected").val();

    console.log(valv, valp)
    $('.change-val').attr("valp",valp)
    $('.change-val').attr("valv",valv)

})


