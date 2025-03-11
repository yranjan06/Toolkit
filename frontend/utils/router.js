const Home = {
    template: `
    <div>
        <h1>Home</h1>
    </div>
    `
}


import LoginPage from '../pages/LoginPage.js';
import RegisterPage from '../pages/RegisterPage.js';
import BlogsListPage from '../pages/BlogsListPage.js';




const routes = [
    {path : '/', component : Home},
    {path : '/login', component : LoginPage},
    {path : '/register', component : RegisterPage},
    {path : '/feed', component : BlogsListPage},
]


const router = new VueRouter({
    routes
});

export default router; 


