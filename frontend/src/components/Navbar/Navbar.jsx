import React, { useState } from 'react';
import { Link } from "react-router-dom";

const Navbar = () => {
    const key = sessionStorage.getItem("key");
    const [showCreateWorkout, setShowCreateWorkout] = useState(false);
    const [showCreateTask, setShowCreateTask] = useState(false);

    return (
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <div className="container-fluid">
                    <Link className="navbar-brand" to="/" onClick={() => {
                                    setShowCreateWorkout(false);
                                    setShowCreateTask(false);
                                }}>Healthy at Home</Link>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>

                    <div className="collapse navbar-collapse" id="navbarNav">
                    {   key === null
                    ?
                        <ul className="navbar-nav">
                            <li className="nav-item">
                                <Link className="nav-link" to="/register" onClick={() => {
                                    setShowCreateWorkout(false);
                                    setShowCreateTask(false);
                                }}>Register</Link>
                            </li>

                            <li className="nav-item">
                                <Link className="nav-link" to="/login" onClick={() => {
                                    setShowCreateWorkout(false);
                                    setShowCreateTask(false);
                                }}>Login</Link>
                            </li>
                        </ul>
                    :
                        <ul className="navbar-nav">
                            <li className="nav-item">
                                <Link className="nav-link" to="/workouts" onClick={() => {
                                    setShowCreateWorkout(true);
                                    setShowCreateTask(false);
                                }}>Workouts</Link>
                            </li>

                            <li className="nav-item">
                                <Link className="nav-link" to="/tasks" onClick={() => {
                                    setShowCreateWorkout(false);
                                    setShowCreateTask(true);
                                }}>Tasks</Link>
                            </li>

                            <li className="nav-item">
                                <Link className="nav-link" to="/profile" onClick={() => {
                                    setShowCreateWorkout(false);
                                    setShowCreateTask(false);
                                }}>Profile</Link>
                            </li>

                            <li className="nav-item">
                                <Link className="nav-link" to="/logout">Logout</Link>
                            </li>
                            {
                                showCreateWorkout && 
                                <li className="nav-item">
                                    <Link className="nav-link" to="/workout/create/">Create Workout</Link>
                                </li>
                            }
                            {
                                showCreateTask &&
                                <li className="nav-item">
                                    <Link className="nav-link" to="/task/create/">Create Task</Link>
                                </li>
                            }
                        </ul>
                    }
                    </div>
                </div>
            </nav>
    );
}

export default Navbar;