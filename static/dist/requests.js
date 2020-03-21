const collectionManagementURL = (collection_id,question_id) => `http://${window.location.host}/collection/${collection_id}/question/${question_id}/`
const createCollectionURL = `http://${window.location.host}/collection/create/`

async function addToCollection(collection_id,question_id){
    try{
    result =await $.post(collectionManagementURL(collection_id,question_id))
    }catch(err){
        alert("Couldn't add to collection")
    }
}

async function removeFromCollection(collection_id,question_id){
    try{
    result = await $.ajax({
        url: collectionManagementURL(collection_id,question_id),
        type: 'DELETE'
    });
    
    }catch(err){
        alert("Couldn't remove from collection")
    }
}

async function createCollectionRequest(name){
    try{
    var result =await $.post(createCollectionURL,{'name':name})
    return result.collection_id
    }catch(err){
        alert("Couldn't create collection")
        return null
    }
}

$.ajaxSetup({
    beforeSend:function(xhr,settings){
        xhr.setRequestHeader("X-CSRFToken",csrf)
    }
})

