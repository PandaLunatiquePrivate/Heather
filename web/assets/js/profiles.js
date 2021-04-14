(window.addEventListener('load', () => {

    const profileContainer = $('#profiles').get(0);
    $.ajax({
        url: `api/v1/heather/profile/list`,
        method: 'GET',
        data: {

        }
    }).done((d, s) => {

        if(d.meta.status_code === 200 && s === 'success') {

            d.result.profiles.forEach((e) => {

                let newProfile = document.createElement('div');
                let profileAvatar = document.createElement('img');
                let profileSpan = document.createElement('span');

                newProfile.id = e.uid;
                newProfile.classList.add('profile');

                profileAvatar.src = 'assets/img/beatrice.jpg';
                profileAvatar.alt = 'Avatar';

                profileSpan.innerHTML = e.name;

                newProfile.appendChild(profileAvatar);
                newProfile.appendChild(profileSpan);

                profileContainer.insertBefore(newProfile, profileContainer.firstChild);

            });

        }
    })

    setTimeout(() => {

        let loadingScreen = $('#loading-screen');
        loadingScreen.css({
            animation: 'loadingFadeOut 0.5s'
        });

        setTimeout(() => {
            
            document.getElementById('loading-screen').remove();
        
        }, 450);

    }, 4000);

}))