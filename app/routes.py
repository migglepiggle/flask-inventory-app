from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import db, InventoryItem
from .forms import InventoryForm

inventory_bp = Blueprint('inventory', __name__, url_prefix='/inventory')

# View All Inventory Items
@inventory_bp.route('/')
def index():
    items = InventoryItem.query.order_by(InventoryItem.name).all()
    return render_template('inventory/index.html', items=items, query='')

# Search Functionality
@inventory_bp.route('/search')
def search():
    query = request.args.get('q', '')
    items = InventoryItem.query.filter(InventoryItem.name.ilike(f'%{query}%')).all()
    return render_template('inventory/index.html', items=items, query=query)

# Add New Inventory Item
@inventory_bp.route('/add', methods=['GET', 'POST'])
def add_item():
    form = InventoryForm()
    if form.validate_on_submit():
        item = InventoryItem(
            name=form.name.data,
            quantity=form.quantity.data,
            unit=form.unit.data,
            category=form.category.data
        )
        db.session.add(item)
        db.session.commit()
        flash('Item added successfully!', 'success')
        return redirect(url_for('inventory.index'))
    return render_template('inventory/add_item.html', form=form)

# Edit Existing Item
@inventory_bp.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = InventoryItem.query.get_or_404(item_id)
    form = InventoryForm(obj=item)
    if form.validate_on_submit():
        item.name = form.name.data
        item.quantity = form.quantity.data
        item.unit = form.unit.data
        item.category = form.category.data
        db.session.commit()
        flash('Item updated successfully!', 'success')
        return redirect(url_for('inventory.index'))
    return render_template('inventory/edit_item.html', form=form, item=item)

# Delete Item
@inventory_bp.route('/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    item = InventoryItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('Item deleted successfully.', 'info')
    return redirect(url_for('inventory.index'))
