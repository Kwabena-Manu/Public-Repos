document.addEventListener('DOMContentLoaded', function () {

  emailview = document.createElement('div');
  emailview.id = 'email-view';
  document.querySelector('#compose-body').rows = "12";
  document.querySelector('.container').appendChild(emailview);
  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  document.querySelector('#compose-form').addEventListener('submit', submit_mail);

  // By default, load the inbox
  load_mailbox('inbox');
});

  
function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#email-view').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';


}

function load_mailbox(mailbox) {

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  check_inbox(mailbox);

}



function submit_mail(event) {
  event.preventDefault();
  const thesubject = document.querySelector('#compose-subject').value;
  const therecipients = document.querySelector('#compose-recipients').value;
  const thebody = document.querySelector('#compose-body').value;

  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify(
      {
        subject: thesubject,
        recipients: therecipients,
        body: thebody,
      }
    ),
  })
  .then(response => response.json())
  .then(result => {
            console.log(result);
        })
  .then(response => load_mailbox('sent'));

  return false;
}



function check_inbox(mailbox) {

  fetch(`/emails/${mailbox}`)
    .then(response => response.json())
    .then(emails => {
      let innercontainer = document.createElement('div');
      innercontainer.className = 'incont';

      if (emails.length == 0) {
        let info = document.createElement('h2')
        info.innerHTML = `There are no ${mailbox} email`;
        document.querySelector("#emails-view").appendChild(info)

      }

      emails.forEach(email => {
        if (mailbox === 'sent' || mailbox === 'archive') {
          set_read(email.id);
        }


        let mailrow = document.createElement('div');
        mailrow.className = "row border border-dark";


        mailrow.innerHTML += `
        <div class="col-10 p-2">
            <div class="row">
                <div class="ml-3">
                ${email.sender}
                </div>
                <div class="ml-3">
                    ${email.subject}
                </div>
            </div>
        </div>
        
        `;




        if (email.read == false) {
          mailrow.style.backgroundColor = 'gray';

        }

        if (mailrow.style.backgroundColor == 'gray') 
        {
          mailrow.innerHTML += `<div class="col-2 p-2">
          ${email.timestamp}
          </div>`;
        }
        else{
          mailrow.innerHTML += `<div class="col-2 p-2 text-muted">
             ${email.timestamp}
        </div>`
        }


        innercontainer.appendChild(mailrow);


        mailrow.onclick = function () {

          set_read(email.id);

          check_mail(email.id, mailbox);
        }

      });
      let pagebody = document.querySelector("#emails-view");
      pagebody.appendChild(innercontainer);
    });
}




function check_mail(id, mailbox) {
  fetch(`/emails/${id}`)
    .then(response => response.json())
    .then(email => {

      document.querySelector('#emails-view').style.display = 'none';
      document.querySelector('#compose-view').style.display = 'none';
      emailview = document.querySelector('#email-view');
      emailview.style.display = 'block';

      emailview.innerHTML = "";
      let archvalue = "";
      if(email.archived === true)
      {
        archvalue = "Unarchive" ;
      }
      else{
        archvalue = "Archive"; 
      }

      emailview.innerHTML += `<div>
      <p>

      <span style="font-weight: bold">From: </span> ${email.sender} <br>
      <span style="font-weight: bold">To: </span> ${email.recipients}<br>
      <span style="font-weight: bold">Subject: </span>${email.subject}<br>
      <span style="font-weight: bold">Timestamp: </span>${email.timestamp}<br>
      <input class="btn btn-sm btn-outline-primary"  id="repbutton" type="submit" value="Reply">
      <input class="btn btn-sm btn-outline-primary"  id="archbutton" type="submit" value="${archvalue}">

      </p>
      
      <hr>

      <br>
  
      <pre>
      ${email.body}
      
      </pre>
      <br><br>
  </div>`;

      if (mailbox != 'sent') {

        arch = document.querySelector('#archbutton');

        arch.onclick = function () {

          fetch(`/emails/${id}`,
            {
              method: 'PUT',
              body: JSON.stringify(
                {
                  archived: !email.archived
                }
              )

            })
            .then(response => load_mailbox('inbox'));




        }



        reply = document.querySelector('#repbutton');

        reply.onclick = function () {
          compose_email();
          let recipients = document.querySelector('#compose-recipients');
          let subject = document.querySelector('#compose-subject');
          let body = document.querySelector('#compose-body');
          bodytext = "";
          bodytext = `\nOn ${email.timestamp} ${email.sender} wrote:\n${email.body}
        \n===============================================`;
          sub = email.subject;

          console.log(sub);

          recipients.value = email.sender;

          first3 = sub.substr(0, 3);

          if (first3.toLowerCase() != 're:') {
            let pre = 'Re: ';
            pre += sub;

            sub = pre;
          }
          subject.value = sub;
          body.value = bodytext;



        }

      }



    });
}




function set_read(id) {
  fetch(`/emails/${id}`,
    {
      method: 'PUT',
      body: JSON.stringify(
        {
          read: true
        }
      )

    })
}






