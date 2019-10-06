import React, { Component } from 'react'

export default class inputChanges extends Component {

  handleAllFormChanges = (props, val) => {
    this.setState({
      [ props ]: val
    })
  }
  render() {
    return (
      <div>
        <input
          placeholder='fancy input box'
          onChange={ e => this.handleAllChanges('description', e.target.value) }
        />
      </div>
    )
  }
}
