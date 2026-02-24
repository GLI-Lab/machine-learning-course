# Machine Learning Course (for students)

The lab environment is set up with **pixi**. Follow the steps below.

---

## 1. Git — Get the repo / Update

### First time (clone)

```bash
git clone -b students https://github.com/GLI-Lab/machine-learning-course.git
cd machine-learning-course
```

### Update (get latest course materials)

If you already cloned the `students` branch, just pull the latest changes:

```bash
git pull   # updates from origin/students when you're on the students branch
```

---

## 2. Pixi — Install environment and run

### If you don't have Pixi (one-time)

- **Install**: https://pixi.sh/latest/getting_started/installation/

### Install project environment

From the repo root (`machine-learning-course`):

```bash
pixi install
```

Dependencies and Jupyter will be installed automatically.

### Run Jupyter Lab

```bash
pixi run jupyter
```

Open the URL shown in your browser

---

## Summary

| When | Command |
|------|---------|
| First-time clone | `git clone -b students https://github.com/GLI-Lab/machine-learning-course.git` → `cd machine-learning-course` |
| Update materials | `git pull` |
| Install environment | `pixi install` |
| Run Jupyter | `pixi run jupyter` |
