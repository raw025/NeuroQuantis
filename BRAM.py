module synapse_memory (
    input logic clk,
    input logic wr_en,
    input logic [9:0] address,
    input logic signed [15:0] data_in,
    output logic signed [15:0] data_out
);
    logic signed [15:0] memory [1023:0];  // 1K synaptic storage  

    always_ff @(posedge clk) begin
        if (wr_en)
            memory[address] <= data_in;
        data_out <= memory[address];
    end
endmodule
