import React from 'react'
import SplitPane from './SplitPane'
import Login from './Login'
import Dashboard from './Dashboard';
import Logs from './Logs';


const App = () => {
   
    const child1 = <SplitPane direction='vertical' child1={<Login/>} child2={<Logs/>}/>
    const child2 = <Dashboard />

    return (
        <div className='container'>
            <SplitPane
                direction='horizontal'
                child1={child1} 
                child2={child2}
            />
        </div>
    )
}

export default App;
