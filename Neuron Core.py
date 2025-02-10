module neuron_core (
    input  logic clk,  
    input  logic rst,  
    input  logic signed [15:0] synaptic_input,  
    input  logic signed [15:0] weight,  
    output logic spike  
);
    logic signed [31:0] membrane_potential;  
    logic signed [15:0] threshold = 16'h1000; // Set thresholds

    always_ff @(posedge clk or posedge rst) begin
        if (rst) 
            membrane_potential <= 0;
        else begin
            membrane_potential <= membrane_potential + synaptic_input * weight;
            if (membrane_potential >= threshold) begin
                spike <= 1;
                membrane_potential <= 0;  // Reset after triggering
            end else begin
                spike <= 0;
            end
        end
    end
endmodule
