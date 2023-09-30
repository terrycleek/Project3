let url = "https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json"

function dropdown_menu(){
    d3.json(url).then((data) => {
    
    
        let names = data.names

        let selector = d3.select("#selDataset");
                
        names.forEach((sample) => {
            selector
                .append("option")
                .text(sample)
                .property("value", sample);
        });
        meta_table(names[0])
        charts(names[0])
    
    })

}
dropdown_menu()

function meta_table(sample_id){
    d3.json(url).then((data) => {
    
    
        let metadata = data.metadata
        let metaarray = metadata.filter(number => number.id == sample_id)[0];

        let selector = d3.select("#sample-metadata");
        selector.html("")

        Object.entries(metaarray).forEach(entry => {
            const [key, value] = entry;
            console.log(key, value);
            selector
                .append("h5")
                .text(` ${key}: ${value}`)
          });


    
    
    })

}

function optionChanged(sample_id){
    meta_table(sample_id)
    charts(sample_id)

}

function charts(sample_id){
    d3.json(url).then((data) => {
    
    
        let samplesdata = data.samples
        let samplesarray = samplesdata.filter(number => number.id == sample_id)[0];

        let otu_ids = samplesarray.otu_ids

        let sample_values = samplesarray.sample_values
        
        let otu_labels = samplesarray.otu_labels
        
        var bubbledata = [{
            x: otu_ids,
            y: sample_values,
            text: otu_labels,
            mode: 'markers',
            marker: {
              color: otu_ids,
              colorscale: "Earth",
              size: sample_values
            }
          }];
          
          
          var bubblelayout = {
            title: 'Bubble Chart',
            showlegend: false,
          };
          
          Plotly.newPlot('bubble', bubbledata, bubblelayout);

          var bardata = [{
            x: sample_values.slice(0,10).reverse(),
            y: otu_ids.slice(0,10).map((index) => `otu ${index}`).reverse(),
            text: otu_labels.slice(0,10).reverse(),
            orientation: 'h',
            type: 'bar'
          }];
          
          
          var barlayout = {
            title: 'Bar Chart',
          };
          
          Plotly.newPlot('bar', bardata, barlayout);
             
    
    
    })

}