import HomePage from './components/HomePage/HomePage'
import Workouts from './components/Workouts/Workouts';
import Workout from './components/Workouts/Workout';
import Tasks from './components/Tasks/Tasks';
import Register from './components/Register/Register';
import Login from './components/Login/Login';
import Logout from './components/Logout/Logout';
import Profile from './components/Profile/Profile';
import Navbar from './components/Navbar/Navbar';
import './App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import DeleteWorkout from './components/Workouts/DeleteWorkout';
import CreateWorkout from './components/Workouts/CreateWorkout';
import EditWorkout from './components/Workouts/EditWorkout';
import Task from './components/Tasks/Task';
import EditTask from './components/Tasks/EditTask';
import CreateTask from './components/Tasks/CreateTask';
import DeleteTask from './components/Tasks/DeleteTask';
import CalorieCounter from './components/Profile/CalorieCounter';

const App = () => {
  return (
    <div className="App">
      <Router>
        <Navbar/>

        <Switch>
          <Route exact path="/" component={HomePage} />

          <Route exact path="/workouts" component={Workouts} />

          <Route exact path="/workout/create" component={CreateWorkout} />

          <Route exact path="/workout/:id" component={Workout} />

          <Route exact path="/workout/:id/edit" component={EditWorkout} />

          <Route exact path="/workout/:id/delete" component={DeleteWorkout} />

          <Route exact path="/tasks" component={Tasks} />

          <Route exact path="/task/create" component={CreateTask} />

          <Route exact path="/task/:id" component={Task} />

          <Route exact path="/task/:id/edit" component={EditTask} />

          <Route exact path="/task/:id/delete" component={DeleteTask} />
          
          <Route exact path="/register" component={Register} />

          <Route exact path="/login" component={Login} />

          <Route exact path="/logout" component={Logout} />

          <Route exact path="/profile" component={Profile} />

          <Route exact path="/calorie-counter" component={CalorieCounter}/>
        </Switch>
      </Router>
    </div>
  );
}

export default App;