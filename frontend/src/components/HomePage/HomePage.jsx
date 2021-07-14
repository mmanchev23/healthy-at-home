import React from 'react';
import 'react-toastify/dist/ReactToastify.css';
import style from "./HomePage.module.css";

const HomePage = () => { 
    const key = sessionStorage.getItem("key");
    return(
        <div  className={style.text}>
            {key === null ? "Not registered" : "Registered"}
        </div>
    );
}

export default HomePage;