var React = require('react')
var ReactDOM = require('react-dom')

var StoreList = React.createClass({
    loadBooksFromServer: function(){
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                console.log("In load function");
                console.log(data)
                this.setState({data: data});
            }.bind(this)
        })
    },

    getInitialState: function() {
        return {data: []};
    },

    componentDidMount: function() {
        console.log("In componentDidMount");
        this.loadBooksFromServer();

    },
    render: function() {
        if (this.state.data) {
            console.log(this.state.data)

        }
        return (
            <div>
                <h1>{this.state.data[0]}</h1>

            </div>
        )
    }
})

ReactDOM.render(<StoreList url='/khaana-peena/react_stores' />,
    document.getElementById('container'));