module noc_mesh (
    input  logic clk,
    input  logic rst,
    input  logic [3:0] neuron_in,  
    output logic [3:0] neuron_out  
);
    always_ff @(posedge clk or posedge rst) begin
        if (rst)
            neuron_out <= 4'b0000;
        else
            neuron_out <= neuron_in;  // Simple data transfer (can be optimized later)
    end
endmodule
