import React, { useState } from 'react';
import { Button } from "reactstrap";
import { useHistory } from "react-router-dom";

const Profile = () => {
    const [user, setUser] = useState([]);
    const history = useHistory();
    
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

    const handleLogout = () => {
        history.push("/logout");
    }

    const redirect = () => {
        history.push("/calorie-counter");
    }

    return(
        <div style={{display: "flex"}}>
            <div style={{flex: "1"}}>
                <img src={user.profile_picture} style={{borderRadius: "50%", width: "300px", height: "auto", margin: "50px 100px 100px 25%"}}></img>

            </div>
            <div style={{flex: "1"}}>
                <h1 style={{margin: "100px 100px 100px 100px", textAlign: "center"}}>{user.first_name} {user.last_name}</h1>
                <div style={{display: "flex"}}>
                    <Button color="primary" style={{flex: "1", margin: "5px 5px 5px 5px"}} onClick={redirect}>Calorie Counter</Button>
                    <Button color="success" style={{flex: "1", margin: "5px 5px 5px 5px"}}>Edit Profile</Button>
                    <Button color="danger" style={{flex: "1", margin: "5px 5px 5px 5px"}} onClick={handleLogout}>Logout</Button>
                </div>
            </div>
        </div>
    );
}

export default Profile;