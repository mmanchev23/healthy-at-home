import React, { useState } from 'react';

const Profile = () => {
    const [user, setUser] = useState([]);
    
    if (user.length === 0) {
        fetch("http://127.0.0.1:8000/credentials/", {
            method: "GET",
            headers: {
                'Authorization': `Token ${sessionStorage.getItem("key")}`
            }
        })
        .then(response => response.json())
        .then(data =>setUser(data.credentials[0]))
    }

    return(
        <div>
            {user.id}
        </div>
    );
}

export default Profile;