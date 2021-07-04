function show_bar_item(){
    item =  document.getElementById('sbar');
    if(item.style.display == 'none'){
        item.style.display = 'block';
    }else{item.style.display='none';}

}
function show_comment(){
    item = document.getElementById('comment')
    if(item.style.display == 'none'){
        item.style.display = 'block';
    }else{item.style.display='none';}
}

function bold(type){
    item = document.getElementById('body_textarea');
    item_initial_value = item.value;
    var SelectionStart =  item.selectionStart;
    var SelectionEnd = item.selectionEnd;
    var SelectedValue = item_initial_value.slice(SelectionStart,SelectionEnd);
    sliecd_value1 = item_initial_value.slice(0,SelectionStart);
    sliecd_value2 = item_initial_value.slice(SelectionEnd,-1);
    if (type=='i'){
        item.value = sliecd_value1+"<i>"+SelectedValue+"</i>"+sliecd_value2;
    }
    if (type=='b'){
        item.value = sliecd_value1+"<b>"+SelectedValue+"</b>"+sliecd_value2;
    }
    
}
function add_image(image_id){
    console.log(image_id)
    item = document.getElementById('body_textarea');
    item_initial_value = item.value;
    var SelectionStart =  item.selectionStart;
    sliecd_value1 = item_initial_value.slice(0,SelectionStart);
    sliecd_value2 = item_initial_value.slice(SelectionStart,-1);
    item.value = sliecd_value1+"IMAGE("+image_id+")"+sliecd_value2;
}
