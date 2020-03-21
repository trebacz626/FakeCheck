$(function () {
    $(".q-collection").on("changed.bs.select", function(e, clickedIndex, newValue, oldValue) {
      var id = $(this).find('option').eq(clickedIndex).data('id');
      var question_id = $(this).find('option').eq(clickedIndex).data('questionid');
      if (newValue){
        addToCollection(id,question_id)
      }else{
        removeFromCollection(id,question_id)
      }
    });
  });

$('.new-collection').click( async function(){
    name = prompt("Nazwa Kolekcji")
    var collection_id = await createCollectionRequest(name)
    if (! collection_id){
        return
    }
    $('.new-collection').each(function(){
        var questionId = $(this).data('questionid')
        var select = $(this).parent().find('select.q-collection').eq(0)
        select.append(`<option data-id="${collection_id}" data-questionid="${questionId}">${name}</option>`);
        select.selectpicker("refresh")
    })

})