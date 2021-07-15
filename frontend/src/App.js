// React and package components
import './App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

// Web app components
import HomePage from './components/HomePage/HomePage';
import Navbar from './components/Navbar/Navbar';
import Register from './components/Register/Register';
import Login from './components/Login/Login';
import Logout from './components/Logout/Logout';
import Profile from './components/Profile/Profile';
import EditProfile from './components/Profile/EditProfile';
import CalorieCounter from './components/CalorieCounter/CalorieCounter';

// Workout sections
import Workouts from './components/Workouts/Workouts';
import Workout from './components/Workouts/Workout';
import CreateWorkout from './components/Workouts/CreateWorkout';
import DeleteWorkout from './components/Workouts/DeleteWorkout';
import EditWorkout from './components/Workouts/EditWorkout';

// Task sections
import Tasks from './components/Tasks/Tasks';
import Task from './components/Tasks/Task';
import CreateTask from './components/Tasks/CreateTask';
import EditTask from './components/Tasks/EditTask';
import DeleteTask from './components/Tasks/DeleteTask';

// BMI sections
import BMIs from './components/BMI/BMIs';
import BMI from './components/BMI/BMI';
import CreateBMI from './components/BMI/CreateBMI';
import EditBMI from './components/BMI/EditBMI';
import DeleteBMI from './components/BMI/DeleteBMI';

// Meal sections
import Meals from './components/Meals/Meals';
import Meal from './components/Meals/Meal';
import CreateMeal from './components/Meals/CreateMeal';
import EditMeal from './components/Meals/EditMeal';
import DeleteMeal from './components/Meals/DeleteMeal';

const App = () => {
  return (
    <div className="App">
      <Router>

        {/* Navbar component */}
        <Navbar/>

        {/* Routing */}
        <Switch>
          
          {/* Web app components */}
          <Route exact path="/" component={HomePage} />
          <Route exact path="/register" component={Register} />
          <Route exact path="/login" component={Login} />
          <Route exact path="/logout" component={Logout} />
          <Route exact path="/profile" component={Profile} />
          <Route exact path="/profile/edit" component={EditProfile} />
          <Route exact path="/calorie-counter" component={CalorieCounter}/>

          {/* Workout sections */}
          <Route exact path="/workouts" component={Workouts} />
          <Route exact path="/workout/:id" component={Workout} />
          <Route exact path="/workout/create" component={CreateWorkout} />
          <Route exact path="/workout/:id/edit" component={EditWorkout} />
          <Route exact path="/workout/:id/delete" component={DeleteWorkout} />

          {/* Task sections */}
          <Route exact path="/tasks" component={Tasks} />
          <Route exact path="/task/:id" component={Task} />
          <Route exact path="/task/create" component={CreateTask} />
          <Route exact path="/task/:id/edit" component={EditTask} />
          <Route exact path="/task/:id/delete" component={DeleteTask} />

          {/* BMI sections */}
          <Route exact path="/bmi-results" component={BMIs}/>
          <Route exact path="/bmi-result/:id" component={BMI}/>
          <Route exact path="/bmi/create" component={CreateBMI}/>
          <Route exact path="/bmi/:id/edit" component={EditBMI} />
          <Route exact path="/bmi/:id/delete" component={DeleteBMI} />

          {/* Meal sections */}
          <Route exact path="/meals" component={Meals}/>
          <Route exact path="/meal/:id" component={Meal}/>
          <Route exact path="/meal/create" component={CreateMeal}/>
          <Route exact path="/meal/:id/edit" component={EditMeal} />
          <Route exact path="/meal/:id/delete" component={DeleteMeal} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;