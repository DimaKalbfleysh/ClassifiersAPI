
function create_classifier(){
    var name = document.getElementById('create_name').value;
    var parent = document.getElementById('create_parent').value;

    $.ajax({
        type: 'GET',
        url: '/api/v1/classifier/create/',
        data: {name: name, parent: parent},
        dataType: 'json',
        contentType: 'application/x-www-form-urlencoded',
        cache: false,
        success: function (json) {
            console.log(json)
        }
    });
}

function create_root_classifier(){
    var name = document.getElementById('create_root_name').value;

    $.ajax({
        type: 'GET',
        url: '/api/v1/classifier/create_root/',
        data: {name: name},
        dataType: 'json',
        contentType: 'application/x-www-form-urlencoded',
        cache: false,
        success: function (json) {
            console.log(json)
        }
    });
}

function get_items(elem) {
    var name_parent = elem.id;
    $.ajax({
        type: 'GET',
        url: '/api/v1/classifier/branch/',
        data: {parent: name_parent},
        dataType: 'json',
        contentType: 'application/x-www-form-urlencoded',
        cache: false,
        success: function (json) {
            console.log(json.data[0].attributes.name);
            var ul = document.createElement('ul');
            for(var i=0; i<json.data.length; i++) {
                var li = document.createElement('li');
                li.innerHTML = json.data[i].attributes.name;
                li.setAttribute('id', json.data[i].attributes.name);
                li.setAttribute('onclick', 'get_items(this)');
                ul.appendChild(li);
            }
            elem.appendChild(ul)
        }
    });
}

function update_path_classifier(){
    var name = document.getElementById('update_name').value;
    var parent = document.getElementById('update_parent').value;
    var new_parent = document.getElementById('update_new_parent').value;

    $.ajax({
        type: 'GET',
        url: '/api/v1/classifier/update_path/',
        data: {name: name, parent: parent, new_parent: new_parent},
        dataType: 'json',
        contentType: 'application/x-www-form-urlencoded',
        cache: false,
        success: function (json) {
            console.log(json)
        }
    });
}

function update_name_classifier(){
    var name = document.getElementById('name').value;
    var parent = document.getElementById('parent').value;
    var new_name = document.getElementById('new_name').value;

    $.ajax({
        type: 'GET',
        url: '/api/v1/classifier/update_name/',
        data: {name: name, parent: parent, new_name: new_name},
        dataType: 'json',
        contentType: 'application/x-www-form-urlencoded',
        cache: false,
        success: function (json) {
            console.log(json)
        }
    });
}

function delete_classifier(){
    var name = document.getElementById('delete_name').value;
    var parent = document.getElementById('delete_parent').value;

    $.ajax({
        type: 'GET',
        url: '/api/v1/classifier/delete/',
        data: {name: name, parent: parent},
        dataType: 'json',
        contentType: 'application/x-www-form-urlencoded',
        cache: false,
        success: function (json) {
            console.log(json)
        }
    });
}
