import React from 'react';


const SplitPane = ({ direction, child1, child2 }) => {
    const style = {
        display: 'flex',
        flexDirection: direction === 'horizontal' ? 'row' : 'column',
        alignItems: 'center',
        justifyContent: 'center',
        width: '100%',
        height: '100%',
    }

    const childStyle = {
        flex: 1,
        width: direction === 'horizontal' ? null : '100%',
        height: direction === 'horizontal' ? '100%' : null,
    }

    const dividerStyle = {
        border: '1px solid rgba(0, 0, 0, 0.3)',
        width: direction === 'horizontal' ? null : '100%',
        height: direction === 'horizontal' ? '100%' : null,
    }

    return (
        <div style={style}>
            <div style={childStyle}>
                { child1 }
            </div>
            <span style={dividerStyle}/>
            <div style={childStyle}>
                { child2 }
            </div>
        </div>
    )

}

export default SplitPane
