#pragma once
#include <iostream>
#include <vector>


struct Connection
{
   double weight;
   double deltaWeight;
};

class Neuron {
   double m_outputVal;
   vector<double> m_outputWeights;

public:
   Neuron(unsigned numOutputs);
};
typedef std::vector<Neuron> Layer;




class Net {
public:
   Net(const std::vector <unsigned> &topology );
   void feedForward(const std::vector <double> &inputVals);
   void backProp(const std::vector<double> &targetVals);
   void getResults(std::vector<double> &resultVals);
   void setNumber();
   //~Net();

private:
   std::vector<Layer> m_layers;
  
};
