
# Readme file for desk

SIT Rolos is an intelligent collaborative platform for using conventional, predictive artificial intelligence (AI) based and quantum computational modelling, which aims to improve research teams’ productivity.

### **What you can do in the project:**

- Write code and conduct experiments at your personal **desk**
- Manage your project **team**
- Convert Jupyter Notebooks with results of your project to **publications**

### What you can do at your desk:

The desk is your personal workspace where you can write and run code in web-IDE, change the computational environment for IDE, create notebooks to convert them to interactive papers.

- **Writing and running code:** Your desk contains web-IDE - VSCode which is launching each time you choose or switch computational environments
- **Versioning of the code in Web-IDE:** When you created this project, Rolos has automatically created a git-repository. Your team works in a common git repository and when you launch your desk for the first time - you see the current state of the repository on your desk. To be further aligned with your team - you can work with your repository as usual - commit, push, and pull changes with VSCode source control manager.
- **Versioning of the data in Web-IDE:** Along with git-repo, Rolos set up DVC for versioning of heavy data. Files bigger than 10Mb will be routed to Rolos S3 storage through DVC
- **Changing environment:** If you need to switch from one environment to another, click on the button in the left corner and choose the template that you want to launch. When you change your computing environments - all files are moving along with you and you can continue working from the point where you stopped in the previous environment. Note that Rolos creates a new environment each time you change it - we don’t save the environment state when you move from one environment to another and back.
- **Custom setup and advanced settings:** In case you need a terminal to access the computational environment to install additional packages or repository to get the previous version or see commits history - use VSCode terminal.
- ***Bonus for Material Science & Life Science Researchers:** Most molecular structure formats can be opened in a 3D visualiser - click on the file with the right button and launch NGL or Protein Viewer.
