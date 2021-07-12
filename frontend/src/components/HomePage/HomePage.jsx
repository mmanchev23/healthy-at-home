import React from 'react';
import { useHistory } from "react-router-dom";
import { ToastContainer, toast, Slide } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import style from "./HomePage.module.css";

const HomePage = (props) => { 
    const history = useHistory();
    const key = sessionStorage.getItem("key");
    const message = (props.location.state && props.location.state.message) !== undefined ? props.location.state.message : "";

    toast.success(message, {
        transition: Slide,
        position: "top-right",
        autoClose: 5000
    })
    
    return(
        <div  className={style.text}>
            {key === null ? "Not registered" : "Registered"}  
            <ToastContainer/>
        </div>
    );
}

export default HomePage;