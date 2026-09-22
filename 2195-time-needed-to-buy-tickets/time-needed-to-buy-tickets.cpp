class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        // Put all the people (indices) in the queue
        queue<int> q;
        for (int i = 0; i < tickets.size(); i++) q.push(i);
        int counter = 0;
        // As long as kth person didn't collect all
        // his tickets keep on simulating
        while (tickets[k] > 0) {
            // Give the first person (queue front the ticket)
            int front = q.front(); // index of person
            q.pop();
            // Give ticket (Means reduce the number of tickets)
            tickets[front]--;

            // If still > 0 send him to the back of the line
            if (tickets[front] > 0) q.push(front);

            // increase the counter
            counter++;
        }
        return counter;
    }
};