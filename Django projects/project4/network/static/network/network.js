document.addEventListener('DOMContentLoaded', function () {

    if(document.querySelector("#postForm")){
        document.querySelector("#postForm").addEventListener('submit', sendPost);   
    }
    if(document.querySelector("#editLink")){
        document.querySelectorAll("#editLink").forEach(button =>{
            button.onclick = editPost
        })
    }
    if(document.querySelector(".likeButton")){

        document.querySelectorAll('.likeButton').forEach(button=>{
            button.onclick = likePost
        })
    }

    if(document.querySelector("#followButton")){
        document.querySelector("#followButton").addEventListener('click',follow);
    }
    // loadPosts();
});

function loadPosts() {
    let postdiv = document.createElement("div");
    postdiv.innerHTML = ` <div class="post container border border-dark p-4 mt-2">
            <div class="h5">Foo</div>
            <div>
                <a href="">Edit</a>
            </div>
            <div>Content</div>
            <div>Date</div>
            <div>Like</div>
            <div>comment</div>
                </div>`;

    for(let i = 0; i < 5; i++){
        document.querySelector("#posts").appendChild(postdiv);
    }

}

function sendPost(event) {
    event.preventDefault();
    const postcontent = document.querySelector("#postContent").value;

    // console.log(postcontent)


    if (postcontent != ""){

            fetch('/addpost', {
                method: 'POST',
                body: JSON.stringify({
                    post: postcontent
                })
            })
                .then(response => response.json())
                .then(result => {
        
                    if( result.message){
                        console.log(result)
                        document.querySelector("#postContent").value ='';
                        document.location.reload(true)
        
                    }
                })
        
            }
            else{
                const alert =  document.querySelector("#emptyPostAlert");

                if(alert.classList.contains('d-none'))
                    document.querySelector("#emptyPostAlert").classList.remove('d-none') 
                
                if(alert.classList.contains('animateAlert'))
                    alert.classList.remove("animateAlert")
                    window.requestAnimationFrame(function() {
                        alert.classList.add('animateAlert');
                        });
            }
            return false;
    }


function editPost(event){
    event.preventDefault();
    const post = event.target
    let postArea = post.parentElement.parentElement.parentElement.querySelector("#postArea")

    if(post.innerHTML == "Edit"){

            console.log(post.parentElement.parentElement.parentElement.querySelector("#postArea"))
    
            let postContent = postArea.innerHTML.trim()
            postArea.innerHTML = ` <textarea class="form-control" id="postTextArea" rows="1" cols=""> ${postContent}</textarea>`
            post.innerHTML = "Save"
    }
    else
    {
        console.log(postArea.querySelector("#postTextArea"))

        let newPost = postArea.querySelector("#postTextArea").value.trim();
        let postid = post.dataset.id
        if (newPost != ""){
            fetch(`/editpost/${postid}`, {
                method: 'POST',
                body: JSON.stringify({
                    post: newPost
                })
            })
                .then(response => response.json())
                .then(result => {
        
                    if( result.message){
                        console.log(result)
                        postArea.innerHTML =  newPost
                        post.innerHTML = "Edit"
        
                    }
                })
        }
        else{

            const alert =  post.parentElement.parentElement.querySelector("#emptyEditAlert");

            if(alert.classList.contains('d-none'))
                document.querySelector("#emptyEditAlert").classList.remove('d-none') 
            
            if(alert.classList.contains('animateAlert'))
                alert.classList.remove("animateAlert")
                window.requestAnimationFrame(function() {
                    alert.classList.add('animateAlert');
                    });
        }

        


    }
    

    return false
}


function likePost(event){
    event.preventDefault()
    const likeButton = event.target
    let postID = likeButton.parentElement.dataset.id
    let likes = likeButton.parentElement.dataset.likes
    
    fetch(`/likepost/${postID}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(result => {
        if( result.message){
            console.log(result)
            if(likeButton.classList.contains("liked")){
                likeButton.classList.remove("liked");
                likeButton.classList.add("unliked");

                let number = parseInt(likes);
                number = number -1;

                likeButton.parentElement.parentElement.querySelector(".likes").innerHTML = number;
                likeButton.parentElement.dataset.likes = number
                
            }
            else{
                likeButton.classList.add("liked");
                likeButton.classList.remove("unliked");
                
                let number = parseInt(likes);
                number = number +1;
                
                likeButton.parentElement.parentElement.querySelector(".likes").innerHTML = number
                likeButton.parentElement.dataset.likes = number
            }
            

        }
    })
    
    return false
}


function follow(event){

    event.preventDefault()
    let followButton = event.target;
    console.log(followButton)
    let followers = followButton.dataset.followers
    let userid = followButton.dataset.userid

    fetch(`/follow/${userid}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(result => {
        if( result.message){
            console.log(result)
            
            if(result.status == 1){
                followButton.innerHTML="Unfollow"
                let number = parseInt(followers)
                number = number + 1;
                document.querySelector("#followers").innerHTML= number;
                followButton.dataset.followers= number
            }
            else {
                followButton.innerHTML = "Follow"
                let number = parseInt(followers)
                number = number - 1;
                document.querySelector("#followers").innerHTML= number;
                followButton.dataset.followers= number
                
            }
        }
    })
}