$(document).ready(function () {
    $('select.product').change(function (e) {

        e.stopImmediatePropagation();
         let selected = $(this).children("option:selected").val()
        //  $district = $('select.district')
        //  $district.children().remove()
        //  $district.append($.parseHTML("<option value=''>-- Chọn Quận/Huyện--</option>"));
 
        //  $project = $('select.project')
        //  $project.children().remove()
        //  $project.append($.parseHTML("<option value='0'>-- Chọn Dự Án--</option>"));
 
         dt = {
             'uid_product': selected,
             'csrfmiddlewaretoken': get_csrfmiddlewaretoken(),
         }
         console.log(dt)
    })

});