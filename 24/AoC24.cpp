#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <sstream>
#include <queue>
#include <math.h>

using std::string, std::vector, std::unordered_map, std::cout, std::endl, std::fstream;

class Gate
{
    string m_w1_name;
    string m_w2_name;
    string m_OP;
    string m_wOut_name;
    int m_w1;
    int m_w2;
    int m_wOut;

public:
    Gate(const string &s1, bool w1, const string &OP, const string &s2, bool w2, const string &out)
    {
        m_w1_name = s1;
        m_w1 = w1;
        m_OP = OP;
        m_w2_name = s2;
        m_w2 = w2;
        m_wOut_name = out;
        m_wOut = -1;
    }
    Gate(const string &s1, const string &OP, const string &s2, const string &out)
    {
        m_w1_name = s1;
        m_OP = OP;
        m_w2_name = s2;
        m_wOut_name = out;
        m_w1 = -1;
        m_w2 = -1;
        m_wOut = -1;
    }
    friend std::ostream &operator<<(std::ostream &os, const Gate g)
    {
        os << "Wire 1:" << g.m_w1_name << " Wire 2: " << g.m_w2_name << " Output Wire: " << g.m_wOut_name;
        return os;
    }
    void setWire(const string &wirename, bool w)
    {
        if (m_w1_name == wirename)
        {
            m_w1 = w;
        }
        else if (m_w2_name == wirename)
        {
            m_w2 = w;
        }
    }
    bool canCalcOutput(unordered_map<string, bool> &wires)
    {
        if (wires.contains(m_w1_name))
        {
            m_w1 = wires[m_w1_name];
        }
        if (wires.contains(m_w2_name))
        {
            m_w2 = wires[m_w2_name];
        }
        if (m_w1 == -1 || m_w2 == -1)
        {
            return false;
        }
        return true;
    }
    void calcOutput(unordered_map<string, bool> &wires)
    {
        if (m_OP == "OR")
        {
            m_wOut = (m_w1 == 1 || m_w2 == 1) ? 1 : 0;
        }
        else if (m_OP == "AND")
        {
            m_wOut = (m_w1 == m_w2 && m_w1 == 1) ? 1 : 0;
        }
        else if (m_OP == "XOR")
        {
            m_wOut = (m_w1 == m_w2) ? 0 : 1;
        }
        else
        {
            std::cerr << "illegal operator encountered" << endl;
        }
        wires[m_wOut_name] = m_wOut;
    }
    bool isOutputSet()
    {
        if (m_wOut == 0 || m_wOut == 1)
        {
            return true;
        }
        return false;
    }
    bool giveOutput()
    {
        if (m_wOut == -1)
        {
            std::cerr << "value not set";
        }
        return (bool)m_wOut;
    }
};

int main()
{
    unordered_map<string, bool> wires;
    vector<Gate> gates;

    string line;
    fstream file("input_alt.txt");
    if (!file.is_open())
    {
        std::cerr << "file not found test" << endl;
        return 1;
    }
    while (getline(file, line))
    {
        // Skip empty lines or lines with only whitespace
        if (line.empty() || line.find_first_not_of(" \t\n\r") == string::npos)
        {
            continue;
        }

        if (line.find(':') != string::npos)
        { // Wire definition
            size_t sep_dp = line.find(':');
            string wire_name = line.substr(0, sep_dp);
            bool wire_value = static_cast<bool>(stoi(line.substr(sep_dp + 1)));
            wires[wire_name] = wire_value;
        }
        else
        { // Gate definition
            size_t firstSpace = line.find(' ');
            string wireIn1 = line.substr(0, firstSpace);

            size_t secondSpace = line.find(' ', firstSpace + 1);
            string op = line.substr(firstSpace + 1, secondSpace - firstSpace - 1);

            size_t thirdSpace = line.find(' ', secondSpace + 1);
            string wireIn2 = line.substr(secondSpace + 1, thirdSpace - secondSpace - 1);

            string wireOut = line.substr(thirdSpace + 4); // Skip " -> " to extract output wire
            gates.emplace_back(wireIn1, op, wireIn2, wireOut);
        }
    }

    cout << gates[0] << endl;
    cout << gates[gates.size() - 1] << endl;

    std::queue<Gate> toCalc;
    for (auto gate : gates)
    {
        if (gate.canCalcOutput(wires))
        {
            gate.calcOutput(wires);
            // cout << "initla einen" << endl;
        }
        else
        {
            toCalc.push(gate);
        }
    }

    cout << "erfolgreochj alles in die queue" << endl;
    while (!toCalc.empty())
    {
        Gate gate = toCalc.front();
        toCalc.pop();
        if (gate.canCalcOutput(wires))
        {
            gate.calcOutput(wires);
            // cout << "found 1 " << endl;
        }
        else
        {
            toCalc.push(gate);
            // cout << "puttin back that: "<< gate<< endl;
        }
    }
    cout << "Erfolg reich alle Wires berechnet " << endl;
    long long erg = 0;
    for (auto &[key, value] : wires)
    {
        if (key[0] == 'z')
        {
            string s = key.substr(1);
            long pos = stoi(s);
            // cout << key << "  " << (long long)(((long long)value) * (long long)pow(2, pos)) << endl;
            erg += ((long)value) * pow(2, pos);
        }
    }

    cout << erg << endl;

    return 0;
}